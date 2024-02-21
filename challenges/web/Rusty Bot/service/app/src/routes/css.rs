pub async fn index() -> actix_web::HttpResponse {
    actix_web::HttpResponse::Ok().body(include_str!("../pages/static/index.css"))
}

pub async fn home() -> actix_web::HttpResponse {
    actix_web::HttpResponse::Ok().body(include_str!("../pages/static/home.css"))
}