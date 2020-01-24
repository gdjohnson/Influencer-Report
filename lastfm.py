import requests, json, time, pandas as pd
from datetime import datetime

# username = "gzuphoesdown"

pause_duration = 0.5

key = "97f2454b452da1dd2984e44d65593737"
url = 'https://ws.audioscrobbler.com/2.0/?method=user.get{}&user={}&api_key={}&limit={}&extended={}&page={}&format=json'
extended = 0 #api lets you retrieve extended data for each track, 0=no, 1=yes
page = 1 #page of results to start retrieving at


def pull_top_tracks(username, limit):
    method = 'toptracks'
    request_url = url.format(method, username, key, limit, extended, page)
    artist_names = []
    track_names = []
    play_counts = []
    response = requests.get(request_url).json()

    #print(response)
    import pdb; pdb.set_trace()
    for item in response[method]['track']:
        artist_names.append(item['artist']['name'])
        track_names.append(item['name'])
        play_counts.append(item['playcount'])

    # top_tracks = pd.DataFrame()
    # top_tracks['artist'] = artist_names
    # top_tracks['track'] = track_names
    # top_tracks['play_count'] = play_counts
    # top_tracks.to_csv('lastfm_project/lastfm_top_tracks.csv', index=None, encoding='utf-8')
    # top_tracks.head()


def pull_top_albums(username, limit):
    method = 'topalbums'
    request_url = url.format(method, username, key, limit, extended, page)
    response = requests.get(request_url).json()
    # print(response)
    albums = []
    for item in response[method]['album']:
        albums.append(item['name'])

    return albums

def check_against_chars(username, from_date, album_name):
    # if the user listened to the album in the 3wks following Sunday review,
    if pull_after_weeks(username, from_date, album_name):
        # and the user did not listen to it in the 3wks preceding,
        new_listener = pull_before_weeks(username, from_date, album_name)
        if new_listener:
            # return album as a match
            return album_name


def pull_after_weeks(username, from_date, album_name):
    newurl = 'https://ws.audioscrobbler.com/2.0/?method=user.get{}&user={}&from={}&to={}&api_key={}&format=json'
    method = 'weeklyalbumchart'
    to_date = int(from_date) + 604800
    start_dates = [int(from_date), to_date, to_date+604800]
    end_dates = [to_date, to_date+604800, to_date+604800+604800]

    i = 0
    while i < 3:
        request_url = newurl.format(method, username, start_dates[i], end_dates[i], key)
        response = requests.get(request_url).json()
        for chart in response['weeklyalbumchart']['album']:
            name = chart['name']
            if name == album_name:
                return True
        i+=1

    return False

def pull_before_weeks(username, end_date, album_name):
    newurl = 'https://ws.audioscrobbler.com/2.0/?method=user.get{}&user={}&from={}&to={}&api_key={}&format=json'
    method = 'weeklyalbumchart'
    start = int(end_date) - (604800*3)
    start_dates = [start, start+604800, start+604800+604800]
    end_dates = [start+604800, start+604800+604800, int(end_date)]

    i = 0
    while i < 3:
        request_url = newurl.format(method, username, start_dates[i], end_dates[i], key)
        response = requests.get(request_url).json()

        for chart in response['weeklyalbumchart']['album']:
            name = chart['name']
            if name == album_name:
                return False
        i+=1

    return True