from lastfm import pull_top_albums, pull_weekly_charts, pull_album_chart
import datetime
import csv

sundata = open('sunday_reviews.csv')
sundata = csv.reader(sundata)

sundata_albums = []

for row in sundata:
    sundata_albums.append((row[0], row[2]))


def main(username):
    matches = find_album_matches(username)
    test_for_time_relevance(username, matches)

def find_album_matches(username):
    top_albums = pull_top_albums(username, 1000)
    matches = []

    for album in top_albums:
        for review in sundata_albums:
            if review[0] == album:
                matches.append(review)

    
    return matches

def test_for_time_relevance(username, matches):
    for match in matches:
        unix_start_date = find_date_range(match[1], username)
        pull_weekly_charts(username, unix_start_date)


def find_date_range(date, username):
    matches = []

    conversion_table = open('time_conversion.csv')
    conversion_table = csv.reader(conversion_table)

    for row in conversion_table:
        if row[0] == date:
            return row[1]

print(main("gzuphoesdown"))
print(main("grahamgjohnson"))