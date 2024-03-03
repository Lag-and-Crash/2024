FROM ubuntu:22.04@sha256:cb2af41f42b9c9bc9bcdc7cf1735e3c4b3d95b2137be86fd940373471a34c8b0 AS app

COPY welcome /app/run
COPY flag /flag

FROM pwn.red/jail
COPY --from=app / /srv
RUN chmod +x /srv/app/run
