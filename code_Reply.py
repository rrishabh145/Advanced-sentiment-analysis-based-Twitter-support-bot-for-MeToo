
import tweepy
import csv

consumer_key = "sdqTIyouyUnswGfQCxKwgkonk"
consumer_secret = "g8lx6HnCuSXva3WA3Iy7vpuo8J1JjZzagmZosAL88pXCQVgbAP"
access_key = "977312693475512323-Gqgcaq10irsLoIQJd12VwpjUO7sLm0T"
access_secret = "G8MEEGtgQzzmN9jEi9jYV5DAX3yENpMGf0DZdmHLUF7oG"

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
                reply_stat = "@%s Support Women Empowerment #MeToo_Supported #HackFest18_Project" % (row['ScreenName'])
                api.update_status(reply_stat, row['Id'])
            
            fileOut.writerow([row['Tweets'],classification1])
