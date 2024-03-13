use actix_web::HttpResponse;
use tinytemplate::TinyTemplate;

#[derive(serde::Serialize)]
struct Context {
    err_msg: String,
}

#[derive(serde::Deserialize)]
struct ErrMsgInfo {
    err_msg: String,
}

#[actix_web::get("/")]
async fn index(info: Option<actix_web::web::Query<ErrMsgInfo>>) -> HttpResponse {
    let mut tt = TinyTemplate::new();
    tt.set_default_formatter(&tinytemplate::format_unescaped);
    tt.add_template("hello", include_str!("../pages/index.html"))
        .unwrap();

    let rendered = tt
        .render(
            "hello",
            &Context {
                err_msg: match info {
                    Some(info) => info.err_msg.clone(),
                    None => "".into(),
                },
            },
        )
        .unwrap();

    actix_web::HttpResponse::Ok()
        .content_type("text/html; charset=utf-8")
        .body(rendered)
}
