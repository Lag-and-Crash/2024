use actix_web::web;

#[derive(serde::Deserialize)]
pub struct ReportInfo {
    url: String,
}

pub async fn report(info: web::Form<ReportInfo>) -> actix_web::HttpResponse {
    _ = awc::Client::default()
        .post(format!(
            "http://{}:{}/visit",
            std::env::var("BOT_ALIAS").unwrap(),
            std::env::var("BOT_PORT").unwrap().parse::<u16>().unwrap()
        ))
        .send_json(&serde_json::json!({
            "url": info.url
        }))
        .await;
    actix_web::HttpResponse::Ok().body("Report sent.")
}
