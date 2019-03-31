#from __future__ import absolute_import, print_function
import tweepy


consumer_key ="JdiNWuJilkltEyx7dw0pabzTb"
consumer_secret="fpPBbkOpXc79AlPizGc4XuN5s5GW1HdZr7c7XSXBl4kK91O7RW"


access_token="971136871-J1bbxHr2ocolO5zkM3gSrpfAMjK639lSu0hsthH6"
access_token_secret="nAjbhswbThQ5j8NuPtwcE1OFVpHHXZ6iGjq99LqtdZBgJ"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)