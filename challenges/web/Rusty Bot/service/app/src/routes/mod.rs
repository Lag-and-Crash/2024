mod login;
mod logout;
mod lookup;
mod register;
mod upload;

pub fn register_user_routes(cfg: &mut actix_web::web::ServiceConfig) {
    cfg.service(
        actix_web::web::scope("/users")
            .service(login::login)
            .service(logout::logout)
            .service(upload::upload_note)
            .service(lookup::lookup_note),
    );
}

mod debug;
mod get_note;
mod home;
mod index;
mod css;

pub fn register_public_routes(cfg: &mut actix_web::web::ServiceConfig) {
    cfg.service(get_note::get_note)
        .service(index::index)
        // .service(debug::debug)
        .service(home::home)
        .service(actix_web::web::resource("/static/index.css").route(
            actix_web::web::get().to(css::index),
        ))
        .service(actix_web::web::resource("/static/home.css").route(
            actix_web::web::get().to(css::home),
        ));
}

mod report;
pub fn register_ratelimited_services<'a>(
    register_gov_cfg: &'a actix_governor::GovernorConfig<
        actix_governor::PeerIpKeyExtractor,
        actix_governor::governor::middleware::NoOpMiddleware<
            actix_governor::governor::clock::QuantaInstant,
        >,
    >,
    adminbot_gov_cfg: &'a actix_governor::GovernorConfig<
        actix_governor::PeerIpKeyExtractor,
        actix_governor::governor::middleware::NoOpMiddleware<
            actix_governor::governor::clock::QuantaInstant,
        >,
    >,
) -> impl FnOnce(&mut actix_web::web::ServiceConfig) + 'a {
    move |cfg| {
        cfg.service(
            actix_web::web::resource("/register")
                .wrap(actix_governor::Governor::new(register_gov_cfg))
                .route(actix_web::web::post().to(register::register)),
        );
        cfg.service(
            actix_web::web::resource("/report_note")
                .wrap(actix_governor::Governor::new(adminbot_gov_cfg))
                .route(actix_web::web::post().to(report::report)),
        );
    }
}
