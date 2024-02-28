
FROM debian:12-slim
RUN apt-get update
ENV TZ=Asia/Singapore
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN ln -s /bin/true /bin/systemctl
RUN apt-get install -y socat build-essential software-properties-common
RUN apt-get update
RUN apt-get install -y racket
RUN raco pkg install --auto http-easy
RUN raco pkg install --auto jni

RUN apt install openjdk-17-jre-headless openjdk-17-jdk -y

COPY notes.txt /flag
COPY project /project
RUN cp -r /usr/lib/jvm/java-17-openjdk-arm64 /usr/lib/jvm/default-java

RUN cd /project && javac bnKCbaBDFLAHldhlasdasd.java jbcdksnkcal.java nckabnclkansdklands.java plmalnnxAS091.java

RUN rm /bin/sh /bin/bash

CMD ["socat", "TCP4-LISTEN:8014,fork", "EXEC:'/bin/racket',pty,stderr"]
