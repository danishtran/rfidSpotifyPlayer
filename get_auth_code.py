from flask import Flask, request
import threading
import webbrowser
from urllib.parse import quote
import os
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("CLIENT_ID")
redirect_uri = os.getenv("REDIRECT_URI")
scope = "user-read-currently-playing user-modify-playback-state playlist-read-private"

app = Flask(__name__)
auth_code = None

@app.route("/callback")
def callback():
  global auth_code
  auth_code = request.args.get("code")
  return "Authorization successful! You can close this window."

def get_auth_url():
  return (
    "https://accounts.spotify.com/authorize"
    f"?response_type=code"
    f"&client_id={quote(client_id)}"
    f"&scope={quote(scope)}"
    f"&redirect_uri={quote(redirect_uri)}"
  )

def run_server():
    app.run(port=5000)

def run():
  threading.Thread(target=run_server).start()
  auth_url = get_auth_url()
  print("Open Website: auth_url")
  webbrowser.open(auth_url)
  while auth_code is None:
    pass
  print("Authorization code:", auth_code)

if __name__ == "__main__":
  run()