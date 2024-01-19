FROM python:3.8.5-slim-buster
RUN pip install pycryptodome
WORKDIR /application
COPY . /application
RUN chmod +x /application/ynetd
EXPOSE 1337
CMD ["/application/ynetd", "-p", "1337", "python3 /application/app.py"]

