FROM debian:stable-slim
RUN apt update
RUN apt upgrade -y
RUN apt install python3 socat -y

WORKDIR /app
COPY files/ /app/
RUN chmod +x /app/server.py
RUN chmod +x /app/ynetd

EXPOSE 1337
CMD ["/app/ynetd", "-p", "1337", "python3 /app/server.py"]
