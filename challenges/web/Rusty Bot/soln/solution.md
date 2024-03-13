## Rusty Robot Solution
The first vulnerability is unsanitised templating on the `/` route with the `err_msg` query parameter.
```rust
let mut tt = TinyTemplate::new();
tt.set_default_formatter(&tinytemplate::format_unescaped);
tt.add_template("hello", include_str!("../pages/index.html")).unwrap();

let rendered = tt.render("hello", &Context {
    err_msg: match info {
        Some(info) => info.err_msg.clone(),
        None => "".into(),
    }
}).unwrap();

actix_web::HttpResponse::Ok()
    .content_type("text/html; charset=utf-8")
    .body(rendered)
```
The tinytemplate formatter used is `format_unescaped` which does not escape HTML. This allows us to perform a reflected XSS attack. However, `index.html` is served with a `'default-src "self"'` CSP, meaning we cannot directly inject code and have it run. Instead, we can make use of the ability to create and access notes to upload a script to a note and use it as a `src` (this falls under `'script-src "self"'`). For example, we can create an account `test_acc:pwd` and upload a note with the contents `alert(1)`. Then, our reflected XSS URL will look like this: `/?err_msg=<script src=/notes?username=test_acc&id=0></script>`, which will trigger an alert pop-up when visited.

However, some basic attacks are mitigated. For instance, directly sending a request to an attacker-owned domain is prevented by the CSP. Instead, we can upload notes to our own account to communicate. Additionally, reading the admin bot's session cookie is blocked because the cookie is `HttpOnly` (default behaviour for `actix_session`). Instead, we need to leak the flag from the bot's account and upload that to a note.

The final piece of the puzzle is finding a way to leak the flag. Directly reading it via the `/notes` endpoint is blocked by the `hidden: true` property. The intended solution is to use a side-channel attack to leak the flag. We first notice that the `/lookup_note` endpoint does not sanitise our input before using it in a regex pattern. While this does not give us an RCE, we can actually use this to trigger a ReDOS attack. The root cause of ReDOS is the backtracking functionality of regex engines. While the `regex` crate which is typically used does not use backtracking, the `fancy-regex` crate does and thus suffers from this vulnerability. Furthermore, we use the ReDOS as an oracle for exfiltrating data (see [this research](https://speakerdeck.com/lmt_swallow/revisiting-redos-a-rough-idea-of-data-exfiltration-by-redos-and-side-channel-techniques)). In a nutshell, we can craft a specific regex pattern that triggers a ReDOS on a specified condition. For example, the slides offer the pattern:
```python
def redos_if(prop):
    return "&(?={})((.*)*)*hoge$".format(prop)
```
Then, we can systematically specify the condition to leak the flag in a manner much like Blind SQLi.

In the provided exploit script, the ReDOS-Leak payload leaks the flag character by character. So, we trigger the XSS over and over again until the entire flag is recovered.

> One thing to keep in mind is that each note has a capacity of at most 1000 characters. If your ReDOS-Leak payload exceeds this length, one solution is to split it into multiple notes across multiple accounts. Since my payload was not too long, I simply minified it.

## Takeaways
This challenge is meant to introduce the player to auditing Rust code. Despite being written in Rust, one likely would not even need to audit the code to find the `err_msg` reflected XSS as it is a common vulnerability. This is a common trend in the challenge -- applying web exploitation concepts often seen in other languages to a foreign language. Next, the player should systematically analyze the "sources" and "sinks" of the program. When they find the regex "sink", it should raise suspicions even if one is not familiar with ReDOS. From here, a POC can be obtained with some Google-fu. The final step is to weave all the pieces together in a program.