FROM ubuntu:18.04@sha256:dca176c9663a7ba4c1f0e710986f5a25e672842963d95b960191e2d9f7185ebe AS app

COPY src /app/run
COPY flag.txt /app/flag.txt

# You don't need to care about this
FROM pwn.red/jail
COPY --from=app / /srv