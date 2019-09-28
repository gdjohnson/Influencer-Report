from pitch_scraper import pitch_scrape
from lastfm import pullTopAlbums

topAlbums = pullTopAlbums("gzuphoesdown", 1000)
sunReviews = pitch_scrape(10)

matches = []

print(topAlbums)
print(sunReviews)

for album in sunReviews['artist']:
    if album == sunReviews:
        matches.append(album)

print(matches)