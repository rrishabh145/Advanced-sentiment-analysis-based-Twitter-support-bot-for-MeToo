
import tweepy
import csv

consumer_key = "LIJqYwhbaoEbzuYRHOxdzyIf7"
consumer_secret = "kmd6C6Rxe4yUCop2ELjrNFti6dRFltq9ZZJRR67sxi7CI2qOaW"
access_key = "976748365231816704-on7uRx0t9It9R2I9LUy6l7jk44qaLaK"
access_secret = "b3LjeN9RTXy1gtqwIRH3z2Oafl4LsNN9oMz2drcusupbK"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)


with open('twitter_classification.csv', 'w', newline = '') as output:

    fileOut = csv.writer(output)
    data = [['Classification','Tweets']]

    fileOut.writerows(data)

    with open('twitter_sentiment_analysis.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if (float(row['Polarity']) < 0.5) and (float(row['Subjectivity']) >=0.25):
                classification1 = "Extreme signs of harrasment/high signs of depression or sadness."
                reply_stat = "@%s Be bold, We are with you. #MeToo_Supported #HackFest18_Project" % (row['ScreenName'])
                api.update_status(reply_stat, row['Id'])
                #print(row['Tweets'])
            elif ((float(row['Polarity']) >= -0.5) and (float(row['Polarity']) < 0.1)) and (float(row['Subjectivity']) >= 0.25):
                    classification1 = "Mild signs of depression/signs of repulsive aggresion."
                    reply_stat = "@%s We are glad that you boldly rose your voice.#MeToo_Supported #HackFest18_Project" % (row['ScreenName'])
                    api.update_status(reply_stat, row['Id'])
            elif (float(row['Polarity']) >= 0.1) and (float(row['Subjectivity']) >=0.25):
                classification1 = "Opposition to the movement."
                reply_stat = "@%s We hope that you believe in women empowerment and their uplifment.#MeToo_Supported #HackFest18_Project" % (row['ScreenName'])
                api.update_status(reply_stat, row['Id'])
            else :
                classification1 = "Neutral/irrelevant to the movement."
                reply_stat = "@%s " % (row['ScreenName'])
                api.update_status(reply_stat, row['Id'])
            
            fileOut.writerow([row['Tweets'],classification1])
