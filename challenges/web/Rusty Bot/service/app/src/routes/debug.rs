#[derive(serde::Deserialize)]
struct Info {
    data: String,
}

#[actix_web::get("/debug")]
async fn debug(
    data: actix_web::web::Data<crate::AppState>,
    info: Option<actix_web::web::Query<Info>>,
) -> impl actix_web::Responder {
    println!(
        "{}",
        match info {
            None => "".into(),
            Some(x) => x.data.clone(),
        }
    );
    actix_web::HttpResponse::Ok().body(format!(
        "Users: {}",
        data.user_manager.read().unwrap().debug()
    ))
}
