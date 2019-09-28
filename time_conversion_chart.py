import requests, json, time, pandas as pd
from datetime import datetime
import numpy as np

# Converts weekly chart Unix start dates to a standard year-month-date format
# Does not need updating


key = "97f2454b452da1dd2984e44d65593737"
extended = 0 #api lets you retrieve extended data for each track, 0=no, 1=yes
page = 1 #page of results to start retrieving at

def pull_weekly_charts(username):
    method = 'weeklychartlist'
    newurl = 'https://ws.audioscrobbler.com/2.0/?method=user.get{}&user={}&api_key={}&format=json'
    request_url = newurl.format(method, username, key)
    response = requests.get(request_url).json()

    str_form = []
    unix_form = []

    for chart in response['weeklychartlist']['chart']:
        unix = int(chart['from'])
        date = datetime.utcfromtimestamp(unix).strftime('%Y-%m-%d')
        unix_form.append(unix)
        str_form.append(date)

    table = {'str': str_form, 'unix': unix_form}
    make_table(table)

def make_table(table):
    frame = pd.DataFrame(data=table)
    print(frame)
    frame.to_csv('./time_conversion.csv', index=None, encoding='utf-8')

pull_weekly_charts('gzuphoesdown')