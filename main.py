from lastfm import pull_top_albums
import csv

sundata = open('sunday_reviews.csv')
sundata = csv.reader(sundata)

sundata_albums = []
for row in sundata:
    sundata_albums.append(row[0])

def find_album_matches(username):
    top_albums = pull_top_albums(username, 1000)
    return list(set(top_albums) & set(sundata_albums)) 

print(find_album_matches("gzuphoesdown"))
print(find_album_matches("grahamgjohnson"))