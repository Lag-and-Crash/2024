FROM python:3-onbuild

RUN pip install pycryptodome

WORKDIR /application
COPY * /application/

CMD ["python","app.py"]
EXPOSE 1337

