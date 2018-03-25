
import tweepy
import csv

#taking credentials of our twitter account which will host the app. 
#
#Get the permission from the author to obtain the keys and other credentials or login to 
#twitter to get your own personal access keys and other credentials
#
consumer_key = "put your key here"
consumer_secret = "put your key here"
access_key = "put your key here"
access_secret = "put your key here"


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
