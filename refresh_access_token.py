from dotenv import load_dotenv
import os
from requests import post
import base64
import json

load_dotenv()

refresh_token = os.getenv("REFRESH_TOKEN")
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def refresh_access_token():
  auth_string = client_id + ":" + client_secret
  auth_bytes = auth_string.encode("utf-8")
  auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")
  url = "https://accounts.spotify.com/api/token"
  headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Authorization": 'Basic ' + auth_base64
  }
  data = {
    "grant_type": "refresh_token",
    "refresh_token": refresh_token,
  }
  result = post(url, headers=headers, data=data)
  json_result = json.loads(result.content)
  access_token = json_result["access_token"].split()[0]
  return access_token

if __name__ == "__main__":
  access_token = refresh_access_token()
  print(access_token)