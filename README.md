# rfidSpotifyPlayer
A Raspberry Pi project that uses RFID tags to control Spotify playback and switch playlists.

## Description
This project lets you scan an RFID tag with a reader connected to a Raspberry Pi. Each tag can be linked to a specific Spotify playlist or playback action such as play, pause, or skip.

## Features
- Map RFID tags to Spotify playlists or actions
- Uses Spotify Web API for playback control
- Stores Spotify API credentials in a local .env file
- Provides scripts to obtain OAuth authorization code, refresh token, and refresh access token
- Designed to run on a Raspberry Pi with an attached RFID reader

## Requirements
- Raspberry Pi with network access
- Python 3.x installed
- RFID reader supported by your Pi
- Raspotify installed
- Spotify Developer account and app
- Internet access on the Pi

Python packages you will need:
- python-dotenv
- requests
- RPi.GPIO
- mfrc522

## Setup
1. Clone the repository:

git clone https://github.com/danishtran/rfidSpotifyPlayer.git
cd rfidSpotifyPlayer

2. Create a Spotify Developer App at https://developer.spotify.com/dashboard/  
   Note the Client ID, Client Secret, and set a Redirect URI such as http://localhost:8888/callback

3. Create a .env file in the project root:

CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret
REDIRECT_URI=your_redirect_uri


4. Make sure your .env file is not committed to version control by adding it to .gitignore.

## Authentication
Run the scripts in this order:

python3 get_auth_code.py
python3 get_refresh_token.py
python3 refresh_access_token.py

- get_auth_code.py guides you to authorize and returns an auth code.
- get_refresh_token.py exchanges the code for a refresh token.
- refresh_access_token.py uses the refresh token to obtain short-lived access tokens and refresh them automatically.

## Running the Project
1. SSH into your Raspberry Pi:

ssh <raspberry_pi_name>

2. Navigate to the project folder:

cd rfidSpotifyPlayer

3. Start the main program:

python3 main.py

The main program initializes the RFID reader, loads mappings, authenticates with Spotify, and listens for tag scans to trigger playback changes.

## Configuration
You can define tag-to-playlist mappings in a JSON, YAML, or Python dictionary. For example:

{
"RFID": "Spotify URI",
}
