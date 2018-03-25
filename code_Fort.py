#Fresh start

import tweepy
import csv
from textblob import TextBlob

#taking credentials of our twitter account which will host the app. 
consumer_key = "sdqTIyouyUnswGfQCxKwgkonk"
consumer_secret = "g8lx6HnCuSXva3WA3Iy7vpuo8J1JjZzagmZosAL88pXCQVgbAP"
access_key = "977312693475512323-Gqgcaq10irsLoIQJd12VwpjUO7sLm0T"
access_secret = "G8MEEGtgQzzmN9jEi9jYV5DAX3yENpMGf0DZdmHLUF7oG"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)

#searching for the #MeToo on the twitter using tweepy library
public_tweets = api.search(q = 'MeToo' , lang = 'en')

#saving the input data into an easy to understand .csv form. 
with open('twitter_sentiment_analysis.csv', 'w', newline = '') as output:

    fileOut = csv.writer(output)
    data = [['ScreenName','Id','Tweets', 'Polarity', 'Subjectivity']]

    fileOut.writerows(data)
#   printing out the specific required fields of the input data.
    for tweet in public_tweets:
        analysis = TextBlob(tweet.text)
        polarity = analysis.sentiment.polarity
        subjectivity = analysis.sentiment.subjectivity
        words = tweet.text.split()
    
        fileOut.writerow([tweet.user.screen_name, tweet.id, tweet.text, polarity, subjectivity])

        # print to terminal
        print (tweet.user.screen_name)
        print (tweet.id)
        print (tweet.text)
        print ('Polarity: ', polarity)
        print ('Subjectivity: ', subjectivity)
        print ('\n\n')
    