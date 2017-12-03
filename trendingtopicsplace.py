import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import csv
import time
import pandas as pd
import datetime
import requests
import json
from __future__ import division
import math
import csv
import matplotlib.pyplot as plt

# Insert your account/app credentials:
consumer_key = 'insert your consumer_key'
consumer_secret = 'insert your consumer_secret'
access_token = 'insert your access_token'
access_secret = 'insert your access_secret'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

# Load file with Where on Earth Id!:
with open('woeid.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile)
    your_list = list(spamreader)
    

# Get trending tweets and save them on csv file indexed according to position in woeid.csv:
j = 1
def get_dic_from_two_lists(keys, values):
    return { keys[s] : values[s] for s in range(len(keys)) }
for n in range(1, len(your_list)):
    i = your_list[n]
    print(i[0])
    tweet = api.trends_place(i[0])
    #print(tweet)
    data = tweet[0]
    trends = data['trends']
    names = [trend['name'] for trend in trends]
    print(names)
    count = [trend['tweet_volume'] for trend in trends]
    dict_try = get_dic_from_two_lists(names, count)
    df = pd.DataFrame.from_dict(dict_try, orient="index")
    filename = "data%d.csv" % (j)
    print(filename)
    df.to_csv(filename)
    j = j+1
    time.sleep( 5 )