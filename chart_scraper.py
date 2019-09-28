import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

page = 'https://last.fm/music/Cat+Power/Moon+Pix/'

def pull_data(uri):
    data = requests.get(uri)

    if data.status_code == 200:
        soup = BeautifulSoup(data.content, 'html.parser')
        listens = grab_listens(soup)
    else:
        print('Status code: %d' % data.status_code)

    frame = make_table(listens)
    grab_change_over_time(listens)


def grab_listens(soup):
    # since 'class' is a reserved word in py, we use 'class_' for search
    date_time = soup.find_all(class_='js-date')
    play_count = soup.find_all(class_='js-value')

    timestamps = {'date': [], 'plays': []}
    
    i=0
    while i < len(date_time):
        date = date_time[i]['datetime']
        plays = int(play_count[i]['data-value'])
        timestamps['date'].append(date)
        timestamps['plays'].append(plays)
        i+=1

    return timestamps

def make_table(listens):
    frame = pd.DataFrame(data=listens)
    print(frame)
    print(" ")
    return frame

def grab_change_over_time(listens):
    plays = listens['plays']
    
    change = []
    max_diff = -1
    max_tup = 0

    i = 1
    while i < len(plays):
        prev_day = plays[i-1]
        curr_day = plays[i]
        diff = round((curr_day - prev_day) / prev_day, 3)
        date = listens['date'][i]
        change.append((date, diff))
        if diff > max_diff:
            max_diff = diff
            max_tup = (date, diff)
        i+=1

    print(change)
    print(" ")
    print(max_tup)

pull_data(page)