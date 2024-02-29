FROM python:3.11-slim-bookworm

COPY app /app

COPY flag.txt /flag.txt

RUN python3 -m pip install -r /app/requirements.txt

RUN groupadd -r app && useradd -r -g app app

RUN chown -R app:app /app && \
    chown -R app:app /flag.txt && \
    chmod 440 /flag.txt && \
    chmod -R 550 /app

USER app

WORKDIR /app

EXPOSE 1337

ENV PYTHONDONTWRITEBYTECODE=1

CMD ["flask", "run", "--host=0.0.0.0", "--port=1337", "--debug", "--no-reload"]