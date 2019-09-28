import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

# Needs to be re-exported to CSV to stay updated with new Sunday reviews

def pitch_scrape(page_limit):
    albums = pull_sundata(page_limit)
    make_table(albums)
    return albums

def pull_sundata(page_limit):
    all_albums = {'date': [], 'artist': [], 'album': []}
    i=1
    while i < page_limit:
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
            all_albums['date'].append(page_dates[j]['datetime'][0:10])
            all_albums['artist'].append(page_artists[j].string)
            all_albums['album'].append(page_albums[j].string)
            
            j+=1

        i+=1

    return all_albums

def make_table(albums):
    frame = pd.DataFrame(data=albums)
    frame.to_csv('./sunday_reviews.csv', index=None, encoding='utf-8')

pitch_scrape(100)