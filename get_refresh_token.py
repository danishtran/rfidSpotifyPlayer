from dotenv import load_dotenv
import os
import base64
from requests import post
import json

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_uri = os.getenv("REDIRECT_URI")
auth_code = os.getenv("AUTH_CODE")
scope = "user-read-currently-playing user-modify-playback-state playlist-read-private"

def get_refresh_token():
  auth_string = client_id + ":" + client_secret
  auth_bytes = auth_string.encode("utf-8")
  auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

  url = "https://accounts.spotify.com/api/token"
  headers = {
    "Authorization": "Basic " + auth_base64,
    "Content-Type": "application/x-www-form-urlencoded"
  }
  data = {
    "grant_type": "authorization_code",
    "code": auth_code,
    "redirect_uri": redirect_uri
  }
  result = post(url, headers=headers, data=data)

  json_result = json.loads(result.content)
  refresh_token = json_result["refresh_token"]
  return refresh_token

if __name__ == "__main__":
  refresh_token = get_refresh_token()
  print(refresh_token)