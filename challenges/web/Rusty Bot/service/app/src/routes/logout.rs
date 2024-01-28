#[actix_web::post("/logout")]
async fn logout(session: actix_session::Session) -> impl actix_web::Responder {
    session.remove("username");
    actix_web::web::Redirect::to("/").see_other()
}
