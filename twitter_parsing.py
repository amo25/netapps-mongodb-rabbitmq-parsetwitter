from __future__ import absolute_import, print_function

# Import modules
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream



consumer_key ="***REMOVED***"
consumer_secret="***REMOVED***"


access_token="***REMOVED***"
access_token_secret="***REMOVED***"

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_status(self, status):
        s=status.text
        print(s)
        print("......")
        s = s.replace('#ECE4564T19', '')
        command = s.split(':')[0]
        therest = s.split(':')[1]
        if('p' in command):
            command = 'p'
            place =therest.split('+')[0]
            print(command)
            print(place)
            therest = therest.split('+')[1]
            stop = therest.find('"')
            print(stop)
            subject = therest[0:stop-1]
            print(subject)
            message = therest[:stop+1]
            print(message)

        elif('c' in command):
            command = 'c'
            place = therest.split('+')[0]
            subject = therest.split('+')[1]
            print(command)
            print(place)
            print(subject)

        return True

    def on_error(self, status_code):
        if status_code == 420:
            return False

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['#ECE4564T19'])