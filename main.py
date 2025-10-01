import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time
import os
from spotify_playback_controller import Spotify

def rfid_id_match(id, spotify):
  playlist_dict = {
    # (RFID): (Spotify URI)
  }

  match id:
    # change case id to RFIDs
    case 1053753130886: # play/pause
      spotify.play_pause_player()
    case 248262475731: # skip next
      spotify.skip_next_playback()
    case 755974389657: # skip back
      spotify.skip_previous_playback()
    case 996307943220: # repeat mode
      spotify.set_repeat_mode()
    case 1041035739071: # shuffle mode
      spotify.set_shuffle_mode()
    case _:  # default case
      if id in playlist_dict: # check id in playlist dictionary
          spotify.play_new_playlist(playlist_dict[id])
      else:
          print("Unknown RFID ID")

def main():
  reader = SimpleMFRC522()
  spotify = Spotify()

  while True:
    try:
      id, _ = reader.read()
      print(id, "Read")
      # change id to RFIDs
      if id == 697975488267: # shutdown pi
        break
      rfid_id_match(id, spotify)
      time.sleep(.5)
    finally:
      GPIO.cleanup()

  os.system("sudo shutdown now")

if __name__ == "__main__":
  main()