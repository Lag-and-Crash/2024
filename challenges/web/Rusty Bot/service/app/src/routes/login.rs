use actix_web::web;

#[actix_web::post("/login")]
async fn login(
    state: web::Data<crate::AppState>,
    info: web::Form<super::register::CredentialsInfo>,
    session: actix_session::Session,
) -> impl actix_web::Responder {
    if state
        .user_manager
        .read()
        .unwrap()
        .find_user(&info.username, &info.password)
    {
        session
            .insert("username", &info.username)
            .expect("Failed to insert into session");
        actix_web::web::Redirect::to("/home").see_other()
    } else {
        actix_web::web::Redirect::to("/?err_msg=Failed to log in").see_other()
    }
}
