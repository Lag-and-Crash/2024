FROM debian:stable-slim
RUN apt update
RUN apt upgrade -y
RUN apt install python3 socat -y

WORKDIR /app
COPY files/ /app/
RUN chmod +x /app/server.py

EXPOSE 1337
CMD ["socat", "TCP-LISTEN:1337,reuseaddr,fork", "EXEC:'/app/server.py',stderr"]
