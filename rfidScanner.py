import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time
import os

reader = SimpleMFRC522()

while True:
  try:
    id, _ = reader.read()
    # change id to RFID
    if id == 697975488267:
      os.system("sudo shutdown now") 
    print(id)
    time.sleep(.5)
  finally:
    GPIO.cleanup()