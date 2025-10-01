from requests import get, post, put
from refresh_access_token import refresh_access_token

class Spotify:
  BASE_URL = "https://api.spotify.com/v1/me/player"

  def __init__(self):
    self.token = refresh_access_token()
    self.repeat_state = "off"
    self.shuffle_state = False
    self.play_pause = False
    self.current_state()

  def _headers_json(self):
    headers = {
      "Authorization": f"Bearer {self.token}",
      "Content-Type": "application/json"
    }
    return headers

  def resume_playback(self):
    url = "https://api.spotify.com/v1/me/player/play"
    headers = self._headers_json()
    result = put(url, headers=headers)

    return result.status_code

  def pause_playback(self):
    url = "https://api.spotify.com/v1/me/player/pause"
    headers = self._headers_json()
    result = put(url, headers=headers)

    if result.status_code == 401:
      self.token = refresh_access_token()
      headers = self._headers_json()
      result = put(url, headers=headers)

    return result.status_code

  def play_pause_player(self):
    if self.play_pause:
      status_code = self.pause_playback()
    else:
      status_code = self.resume_playback()

    self.play_pause = not self.play_pause

    return status_code

  def play_new_playlist(self, context_uri, device_id=None):
    if device_id:
      url = f"https://api.spotify.com/v1/me/player/play?device_id={device_id}"
    else:
      url = "https://api.spotify.com/v1/me/player/play"
    headers = self._headers_json()
    data = {
      "context_uri": context_uri,
    }
    result = put(url, headers=headers, json=data)

    if result.status_code == 401:
      self.token = refresh_access_token()
      headers = self._headers_json()
      result = put(url, headers=headers, json=data)

    return result.status_code

  def skip_next_playback(self):
    url = "https://api.spotify.com/v1/me/player/next"
    headers = self._headers_json()
    result = post(url, headers=headers)
    if result.status_code == 401:
      self.token = refresh_access_token()
      headers = self._headers_json()
      result = post(url, headers=headers)

    return result.status_code

  def skip_previous_playback(self):
    url = "https://api.spotify.com/v1/me/player/previous"
    headers = self._headers_json()
    result = post(url, headers=headers)

    if result.status_code == 401:
      self.token = refresh_access_token()
      headers = self._headers_json()
      result = post(url, headers=headers)

    return result.status_code

  def set_repeat_mode(self):
    repeat_cycle = {
      "off": "context",
      "context": "track",
      "track": "off"
    }
    url = f"https://api.spotify.com/v1/me/player/repeat?state={repeat_cycle[self.repeat_state]}"
    headers = self._headers_json()
    result = put(url, headers=headers)

    if result.status_code == 401:
      self.token = refresh_access_token()
      headers = self._headers_json()
      result = put(url, headers=headers)

    self.repeat_state = repeat_cycle[self.repeat_state]

    return result.status_code

  def set_shuffle_mode(self):
    url = f"https://api.spotify.com/v1/me/player/shuffle?state={(str(not self.shuffle_state)).lower()}"
    headers = self._headers_json()
    result = put(url, headers=headers)

    if result.status_code == 401:
      self.token = refresh_access_token()
      headers = self._headers_json()
      result = put(url, headers=headers)

    self.shuffle_state = not self.shuffle_state
    return result.status_code

  def current_state(self):
    url = "https://api.spotify.com/v1/me/player"
    headers = self._headers_json()
    result = get(url, headers=headers)

    if result.status_code == 204:
      self.play_new_playlist("spotify:playlist:3RbWDgC5LklUgyc5cNs9K3", "f3c7680d97cbe5db191a8a6861b7faa21c623b4f")
      result = get(url, headers=headers)
    elif result.status_code == 401:
      self.token = refresh_access_token()
      headers = self._headers_json()
      result = get(url, headers=headers)

    json_result = result.json()
    self.repeat_state = json_result["repeat_state"]
    self.shuffle_state = json_result["shuffle_state"]
    self.play_pause = json_result["is_playing"]
    return result.status_code

if __name__ == "__main__":
  spotify = Spotify()
  print(spotify.play_pause_player())