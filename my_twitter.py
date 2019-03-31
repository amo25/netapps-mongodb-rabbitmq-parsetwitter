#from __future__ import absolute_import, print_function

# Import modules
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream




consumer_key ="***REMOVED***"
consumer_secret="***REMOVED***"


access_token="***REMOVED***"
access_token_secret="***REMOVED***"

class StdOutListener(StreamListener):
    #reads tweets
    def on_status(self, status):
        s=status.text
        print(s)
        return True

    #returns if too many attempts are made to connect to the API stream
    def on_error(self, status_code):
        if status_code == 420:
            return False

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=[hashtag])
