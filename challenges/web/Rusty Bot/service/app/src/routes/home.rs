use actix_web::HttpResponse;

#[actix_web::get("/home")]
async fn home(session: actix_session::Session) -> HttpResponse {
    if let Ok(Some(_)) = session.get::<String>("username") {
        actix_web::HttpResponse::Ok()
            .content_type("text/html; charset=utf-8")
            .body(include_str!("../pages/home.html"))
    } else {
        actix_web::HttpResponse::Found()
            .append_header(("Location", "/"))
            .finish()
    }
}
