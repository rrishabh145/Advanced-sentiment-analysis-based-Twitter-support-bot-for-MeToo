#Fresh start

import tweepy
import csv
from textblob import TextBlob

#taking credentials of our twitter account which will host the app. 
access_token = "976748365231816704-on7uRx0t9It9R2I9LUy6l7jk44qaLaK"
access_token_secret = "b3LjeN9RTXy1gtqwIRH3z2Oafl4LsNN9oMz2drcusupbK"
consumer_key = "LIJqYwhbaoEbzuYRHOxdzyIf7"
consumer_secret = "kmd6C6Rxe4yUCop2ELjrNFti6dRFltq9ZZJRR67sxi7CI2qOaW"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

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
    
