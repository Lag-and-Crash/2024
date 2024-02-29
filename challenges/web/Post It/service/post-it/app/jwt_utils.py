import jwt
from flask import request


KEYS = {
  "privkey": open("keys/priv.pem").read().strip(),
  "key": open("keys/pub.pem").read().strip()
}


def encode_jwt(payload, key_type="RS256"):
  return jwt.encode(
    payload,
    key=KEYS["privkey"],
    algorithm=key_type
  )


def decode_jwt(token):
  alg = jwt.get_unverified_header(token)["alg"]
  return jwt.decode(
    token,
    key=KEYS["key"],
    algorithms=[alg],
  )
  

def is_logged_in():
  token = request.cookies.get("post_it_token")
  
  if not token:
    return False
  
  try:
    data = decode_jwt(token)
    return {
      "username": data["username"],
      "admin": data["admin"]
    }
  except Exception as e:
    print(e)
    return False


jwt.get_algorithm_by_name("HS256").prepare_key = lambda k: k if isinstance(k, bytes) else k.encode("utf-8")