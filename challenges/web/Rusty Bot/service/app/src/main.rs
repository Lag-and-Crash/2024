use actix_session::{storage::CookieSessionStore, SessionMiddleware};
use actix_web::{web, App, HttpServer};
use std::sync::{Arc, RwLock};
mod routes;
mod user_manager;
use std::env;
use user_manager::*;

struct AppState {
    user_manager: Arc<RwLock<UserManager>>,
}

impl AppState {
    pub fn new(um: UserManager) -> Self {
        Self {
            user_manager: Arc::new(RwLock::new(um)),
        }
    }
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    dotenv::from_filename("../../.env").ok();

    let mut user_manager = UserManager::new(200, 2, 1000);
    let mut admin_user = User::new("admin".into(), env::var("ADMIN_PASSWORD").unwrap());
    admin_user.set_max_notes(2);
    admin_user
        .add_note(env::var("FLAG").unwrap(), true)
        .unwrap();
    admin_user
        .add_note("Lorem ipsum dolor sit amet".into(), false)
        .unwrap();
    user_manager.add_permanent_user(admin_user);

    let state = web::Data::new(AppState::new(user_manager));
    let secret_key = actix_web::cookie::Key::generate();
    let register_governor_conf = actix_governor::GovernorConfigBuilder::default()
        .per_second(10)
        .burst_size(1)
        .finish()
        .unwrap();
    let adminbot_governor_conf = actix_governor::GovernorConfigBuilder::default()
        .per_second(20)
        .burst_size(1)
        .finish()
        .unwrap();

    let port = env::var("SERVER_PORT").unwrap().parse::<u16>().unwrap();
    println!("Actix server listening on port: {port}");
    HttpServer::new(move || {
        App::new()
            .wrap(
                SessionMiddleware::builder(CookieSessionStore::default(), secret_key.clone())
                    .cookie_secure(false)
                    .build(),
            )
            .app_data(state.clone())
            .configure(routes::register_user_routes)
            .configure(routes::register_public_routes)
            .configure(routes::register_ratelimited_services(
                &register_governor_conf,
                &adminbot_governor_conf,
            ))
            .default_service(web::to(actix_web::HttpResponse::NotFound))
    })
    .bind(("0.0.0.0", port))?
    .run()
    .await
}
