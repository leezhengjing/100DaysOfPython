from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
import os


SPOTIPY_CLIENT_ID = os.environ["SPOTIPY_CLIENT_ID"]
SPOTIPY_CLIENT_SECRET = os.environ["SPOTIPY_CLIENT_SECRET"]
SPOTIPY_REDIRECT_URI = os.environ["SPOTIPY_REDIRECT_URI"]

scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=scope,
                                               show_dialog=True,
                                               cache_path="token.txt"))

user_id = sp.current_user()["id"]

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

top_100_URL = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")

songs_webpage = top_100_URL.text

soup = BeautifulSoup(songs_webpage, 'html.parser')
titles = soup.select("h3.c-title.a-no-trucate")
song_titles = [title.getText().replace('\n', '') for title in titles]

year = date.split("-")[0]

SEARCH_API_ENDPOINT = "https://api.spotify.com/v1/search"

with open("token.txt", mode="r") as file:
    content = file.read()
    token = content.split(",")[0].split(":")[1].strip().replace('"', "")

song_uris = []

for song in song_titles:
    result = sp.search(q=song)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify, Skipped")

print(song_uris)

playlist_id = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist_id)

sp.playlist_add_items(playlist_id=playlist_id["id"], items=song_uris)
# params = {
#     "q": song,
#     "type": "track",
# }
# headers = {
#     "Authorization": 'Bearer ' + token
# }
# response = requests.get(url=SEARCH_API_ENDPOINT, params=params, headers=headers)
# data = response.json()
# print(data)
# try:
# except:
#     pass
# else:
#     pass
