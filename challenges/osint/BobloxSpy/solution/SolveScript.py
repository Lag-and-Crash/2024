import requests

# https://users.roblox.com/v1/users/5447870123 1
# https://users.roblox.com/v1/users/5447870850 2
# https://users.roblox.com/v1/users/5447871690 3
descriptions = []
for i in range(2000):
    robloxid = 5447870120 + i
    print(robloxid)
    response = requests.get(f'https://users.roblox.com/v1/users/{robloxid}', headers={'Content-Type': 'application/json'})
    response_json = response.json()
    try:
        if response_json['description'].startswith("LagNCrash"):
            descriptions.append(response_json['description'])
            print(response_json['description'])
            print(descriptions)
    except:
        continue

print(descriptions)