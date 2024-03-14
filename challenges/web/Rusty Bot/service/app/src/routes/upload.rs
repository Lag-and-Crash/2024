use actix_web::http::header::HeaderValue;

#[derive(serde::Deserialize)]
struct NoteInfo {
    contents: String,
}

#[actix_web::post("/upload_note")]
async fn upload_note(
    state: actix_web::web::Data<crate::AppState>,
    info: actix_web::web::Form<NoteInfo>,
    session: actix_session::Session,
    req: actix_web::HttpRequest,
) -> actix_web::Result<String> {
    Ok(if let Some(username) = session.get::<String>("username")? {
        match state.user_manager.write().unwrap().add_note_for_user(
            &username,
            &info.contents,
        ) {
            Err(err) => err,
            Ok(id) => format!(
                "Uploaded note. You can access it at {}/note?id={}&username={}",
                req.headers()
                    .get("origin")
                    .get_or_insert(&HeaderValue::from_str("").unwrap())
                    .to_str()
                    .ok()
                    .get_or_insert(""),
                id,
                username
            ),
        }
    } else {
        "Log in first".into()
    })
}
