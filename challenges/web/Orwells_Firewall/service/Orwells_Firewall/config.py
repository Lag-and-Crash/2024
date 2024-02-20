import os
import secrets

basedir = os.path.abspath(os.path.dirname(__file__))
SECRET_KEY = secrets.token_urlsafe(32)


class Config:
    SECRET_KEY = SECRET_KEY
