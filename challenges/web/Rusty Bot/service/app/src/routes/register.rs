#[derive(serde::Deserialize)]
pub struct CredentialsInfo {
    pub username: String,
    pub password: String,
}

// #[actix_web::post("/register")]
pub async fn register(
    state: actix_web::web::Data<crate::AppState>,
    info: actix_web::web::Form<CredentialsInfo>,
) -> actix_web::HttpResponse {
    actix_web::HttpResponse::Ok().body(
        if state
            .user_manager
            .write()
            .unwrap()
            .add_user(&info.username, &info.password)
            .is_ok()
        {
            "Successfully created account"
        } else {
            "Registration failed"
        },
    )
}
