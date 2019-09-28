import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

def pitch_scrape:
    albums = pull_sundata()
    make_table(albums)

def pull_sundata():
    all_albums = {'date': [], 'artist': [], 'album': []}
    i=1
    while i < 8:
        sundata = requests.get('https://pitchfork.com/reviews/sunday/?page=%d' % i)
        if sundata.status_code != 200:
            print('Page %d not found: status %s' % (i, sundata.status_code))
            break

        sundata = BeautifulSoup(sundata.content, 'html.parser')
        page_artists = sundata.find_all(class_='review__title-artist')
        page_albums = sundata.find_all(class_='review__title-album')
        page_dates = sundata.find_all(class_='pub-date')

        j = 0
        while j < len(page_albums):
            all_albums['date'].append(page_dates[j]['datetime'])
            all_albums['artist'].append(page_artists[j].string)
            all_albums['album'].append(page_albums[j].string)
            
            j+=1

        i+=1

    return all_albums

pull_sundata()