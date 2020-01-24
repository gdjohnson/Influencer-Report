from lastfm import pull_top_albums, pull_after_weeks, pull_before_weeks, check_against_chars
import datetime
import csv

# All Sunday Review albums. The CSV is formatted as [album, artist, date]


def main(username):
    # Loads Sunday review data
    sundata = load_sundata()

    # Finds all album matches btwn Sun Reviews & user listening
    matches = find_album_matches(username, sundata) 
    
    # Checks if users began or heightened listened after Sun Review (incomplete)
    time_relevant_matches = test_for_time_relevance(username, matches)
    
    # matches will have a list of albums; we can calculate matches.length() and 


def load_sundata():
    sundata_csv = open('sunday_reviews.csv')
    sundata_csv = csv.reader(sundata_csv)
    sundata = []
    for row in sundata_csv:
        # Append tuples with album and date for verification against user behavior
        sundata.append((row[0], row[2]))

    return sundata

def find_album_matches(username, sundata):
    top_albums = pull_top_albums(username, 1000) #1000 API limit
    matches = []

    for album in top_albums:
        for review in sundata:
            if review[0] == album:
                matches.append(review)

    return matches

def test_for_time_relevance(username, matches):
    time_relevant_matches = []
    print("ALL MATCHES: ")
    print(matches)
    for match in matches:
        unix_start_date = find_date_range(match[1], username) # We pass Sunday review date via match[1]
        survivor = check_against_chars(username, unix_start_date, match[0])
        if survivor:
            time_relevant_matches.append(survivor)
    
    """    
    time_relevant_matches are: 
        1) in both user library & sunday reviews
        2) were listened to by user in 3wks following sunday review
        3) did not listen to it the 3wks before
    """
    print(time_relevant_matches)
    return time_relevant_matches

def find_date_range(date, username):
    matches = []
    # uses unix to date str conversion table to get a unix timestamp
    # for searching user's weekly charts to note change in behavior
    conversion_table = open('time_conversion.csv')
    conversion_table = csv.reader(conversion_table)

    for row in conversion_table:
        #grabs unix timestamps of weekly chart start time
        #for all user's albums that have been sunday reviewed
        if row[0] == date:  #if Sun Review date matches weekly chart start date
            return row[1]   #then we return the chart start date in unix


print("paul's matches")
main("gzuphoesdown")
print("graham's matches")
main("grahamgjohnson")
# main("YoungTheHuman")
# main("marcosavc")
# main("timbadlose")
# 
# main("canadaaustin")
# main("alyssagen")
# main("thebad69")