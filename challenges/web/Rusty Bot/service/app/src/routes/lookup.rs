#[derive(serde::Deserialize)]
struct LookupNoteInfo {
    contains: String,
}

#[actix_web::post("/lookup_note")]
async fn lookup_note(
    state: actix_web::web::Data<crate::AppState>,
    info: actix_web::web::Form<LookupNoteInfo>,
    session: actix_session::Session,
) -> actix_web::Result<String> {
    Ok(if let Some(username) = session.get::<String>("username")? {
        match state
            .user_manager
            .read()
            .unwrap()
            .find_note_for_user(&username, &info.contains)
        {
            Ok(results) => format!("{:?}", results),
            Err(s) => s,
        }
    } else {
        "Log in first".into()
    })
}
