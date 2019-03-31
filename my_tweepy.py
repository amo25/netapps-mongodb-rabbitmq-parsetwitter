#from __future__ import absolute_import, print_function
import tweepy


consumer_key ="***REMOVED***"
consumer_secret="***REMOVED***"


access_token="***REMOVED***"
access_token_secret="***REMOVED***"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)