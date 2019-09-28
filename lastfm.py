import requests, json, time, pandas as pd

key = "97f2454b452da1dd2984e44d65593737"
username = "gzuphoesdown"

pause_duration = 0.5

url = 'https://ws.audioscrobbler.com/2.0/?method=user.get{}&user={}&api_key={}&limit={}&extended={}&page={}&format=json'
limit = 200 #api lets you retrieve up to 200 records per call
extended = 0 #api lets you retrieve extended data for each track, 0=no, 1=yes
page = 1 #page of results to start retrieving at

method = 'toptracks'
request_url = url.format(method, username, key, limit, extended, page)
artist_names = []
track_names = []
play_counts = []
response = requests.get(request_url).json()

print(response)
import pdb; pdb.set_trace()
for item in response[method]['track']:
    artist_names.append(item['artist']['name'])
    track_names.append(item['name'])
    play_counts.append(item['playcount'])

top_tracks = pd.DataFrame()
top_tracks['artist'] = artist_names
top_tracks['track'] = track_names
top_tracks['play_count'] = play_counts
top_tracks.to_csv('lastfm_project/lastfm_top_tracks.csv', index=None, encoding='utf-8')
top_tracks.head()
