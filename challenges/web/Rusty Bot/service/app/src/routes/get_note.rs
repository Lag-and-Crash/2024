#[derive(serde::Deserialize)]
struct NoteIdInfo {
    username: String,
    id: usize,
}
#[actix_web::get("/note")]
async fn get_note(
    state: actix_web::web::Data<crate::AppState>,
    info: actix_web::web::Query<NoteIdInfo>,
) -> actix_web::Result<String> {
    Ok(
        match state
            .user_manager
            .read()
            .unwrap()
            .get_note_for_user(&info.username, info.id)
        {
            Ok(s) | Err(s) => s,
        },
    )
}
