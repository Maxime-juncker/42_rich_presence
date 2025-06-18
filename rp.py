import requests
from pypresence import Presence
import time
import json
import sys


import json

if (len(sys.argv) != 2):
	print("usage: python3 <script.py> <config.json>")
	sys.exit()
	
with open(sys.argv[1]) as f:
    file = json.load(f)

UID = file["UID"]
SECRET = file["SECRET"]

login = file["login"]

data = {
	"grant_type" : "client_credentials",
	"client_id" : UID,
	"client_secret" : SECRET,
}

response = requests.post("https://api.intra.42.fr/oauth/token", data=data)
if (response.status_code != 200):
	raise Exception("request failed")

code = response.json()["access_token"]
print("access token aquired: " + code)
print(json.dumps(response.json(), indent=4))

header = {
	"Authorization": "Bearer " + code,
}

url = "https://api.intra.42.fr/v2/users?&filter[login]=%s" % login
response = requests.get(url, headers=header)
if (response.status_code != 200):
	raise Exception("request failed")

user = response.json()[0]
print("\nuser infos aquired: ")
print(json.dumps(response.json(), indent=4))



userid = user["id"]
response = requests.get("https://api.intra.42.fr/v2/users/191603/titles", headers=header)
if (response.status_code != 200):
	raise Exception("request failed")

titles = response.json()[0]
title = titles["name"][0:titles["name"].find("%login") - 1]
start = int(time.time())
RPC = Presence("1383806236763623496")
RPC.connect()
print("RPC is online")


#
## Choose which infos to show
#

login = title + " " + login
wallet = "wallet: " + str(user["wallet"])
state = "location: " + (user["location"] or "unavailable")
rank = "rank: " + str(user["kind"])
pp = user["image"]["link"] # your intra picture

RPC.update(
	details=state,
	state=rank,
	start=start,
	large_image = "42", # big 42 image
	small_image=pp,
)
print("RPC is setup")

while True:
	time.sleep(15)
