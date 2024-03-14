FROM ubuntu:22.04@sha256:cb2af41f42b9c9bc9bcdc7cf1735e3c4b3d95b2137be86fd940373471a34c8b0 AS ub
RUN mkdir /app 
COPY BinX.bin /app/run
COPY flag.txt /app/
COPY pass.txt /app/
RUN chmod +x /app/run

# use the jail base image
FROM pwn.red/jail
# copy the root files from any Docker image
COPY --from=ub / /srv
