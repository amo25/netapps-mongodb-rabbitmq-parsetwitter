#Filename: repository.py
#Description: client
#ECE 4564 - Assignment 2
#Team 19 : Alexander Orlov, Maura Hartmann, Mark Owen

# DEPENDENCIES
import RPi.GPIO as GPIO
import time
import sys
import pymongo                      # for nosql
import json
import pika                         # for rabbitmq
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import re
#import captureKeys
from captureKeys import *

RED = 16
GREEN = 20
BLUE = 21

# GPIO
def setGPIO():
    channels=[RED, GREEN, BLUE]
    GPIO.setmode(GPIO.BCM) #Cable labeled with BCM numbers
    GPIO.setup(channels, GPIO.OUT, initial=GPIO.LOW)

# LED STATUS
def set_led(number):
    # white = waiting for a command
    if number == 0:
        GPIO.output(RED, GPIO.HIGH)
        GPIO.output(GREEN, GPIO.HIGH)
        GPIO.output(BLUE, GPIO.HIGH)
    # red = received publish request
    elif number == 1:
        GPIO.output(RED, GPIO.HIGH)
        GPIO.output(GREEN, GPIO.LOW)
        GPIO.output(BLUE, GPIO.LOW)
    # green = received consume request
    elif number == 2:
        GPIO.output(RED, GPIO.LOW)
        GPIO.output(GREEN, GPIO.HIGH)
        GPIO.output(BLUE, GPIO.LOW)

        
        
#inserts a message to mongoDB
def db_insert(Action, Place, Subject, Message):
    ticks = time.time()
    MsgID = "19" + "$" + str(ticks)

    insert_json = {
        "Action": Action,
        "Place": Place,
        "MsgID": MsgID,
        "Subject": Subject,
        'Message': Message
        }

    client = pymongo.MongoClient()
    db = client[Place]
    collection = db[Subject]
    collection.insert_one(insert_json)
    return insert_json

#Rabbit MQ
#Prerequisite: exchanges, bindings, and queue's must be set up
#Another function can be made for this, or we can use the web based gui
def produce(host, Place, Subject, Message):
    credentials = pika.PlainCredentials('Alex', '<removed>')
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=host, credentials=credentials)) #todo modify to connect pi's
    channel = connection.channel()

    channel.basic_publish(
        exchange=Place, routing_key=Subject, body=Message)
    print(" [x] Sent %r:%r" % (Subject, Message))
    connection.close()
    
def consume(host, Place, Subject):
    credentials = pika.PlainCredentials('Alex', '<removed>')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=host, credentials=credentials)) #todo replace with ip
    channel = connection.channel()
    #get all available messages then quit
    while(True):
        (method, properties, body) = channel.basic_get(queue=Subject, auto_ack=True)
        if (method == None):
            break
        else:
            print("%r:%r" % (method.routing_key, body))
        

#parse the tweet
def parse_tweet(original_tweet, hashtag):
    s = re.sub("\s*"+hashtag+"\s*","",original_tweet)
    command = s.split(':')[0]
    command = command.strip() #strip removes whitespace from beginning or end of a character
    therest = s.split(':')[1]
    Place = therest.split('+')[0]
    Place = Place.strip()
    therest = therest.split('+')[1]
    if (command == 'p'):
        Subject = therest.split('\"')[0]
        Subject = Subject.strip()
        Message = therest.split('\"')[1]
        Message.strip()
    elif (command == 'c'):
        Subject = therest.strip()
        Message = None
    
    return (command, Place, Subject, Message)
    

#Twitter stuff
class StdOutListener(StreamListener):
    #reads tweets
    def on_status(self, status):
        original_tweet=status.text #read the tweet
        
        print("[Checkpoint 01 " + str(time.time()) + "] Tweet captured:" + original_tweet)
        #parse the tweet
        (Action, Place, Subject, Message) = parse_tweet(original_tweet, hashtag)
        
        #Store in mongoDB
        json_string = db_insert(Action,Place,Subject,Message)
        print("[Checkpoint 02 " + str(time.time()) + "] Store command in MongoDB instance: " + str(json_string))
        
        print("[Checkpoint 03 " + str(time.time()) + "] GPIO LED: ")
        if (Action == 'p'):
            print("[Checkpoint 04 " + str(time.time()) + "] Produce, Place=" + Place + ", Subject=" + Subject + ", Message=" + Message)
            set_led(1)
            print("[Checkpoint 05 " + str(time.time()) + "]")
            produce(host, Place, Subject, Message)
            time.sleep(1)
            set_led(0)
            
        elif (Action == 'c'):
            print("[Checkpoint 04 " + str(time.time()) + "] Consume, Place=" + Place + ", Subject=" + Subject)
            set_led(2)
            print("[Checkpoint 05 " + str(time.time()) + "]")
            consume(host, Place, Subject)
            time.sleep(1)
            set_led(0)
        
        return True

    #returns if too many attempts are made to connect to the API stream
    def on_error(self, status_code):
        if status_code == 420:
            print("Too many attempts made to connect to Twitter API stream. Wait a bit")
            return False
        
#init
setGPIO()
#arguments
if len(sys.argv) == 5:
    host = sys.argv[2]
    hashtag = sys.argv[4]
else:
    print("Argument format error. Use: python3 capture.py -s <SERVER_IP> -t \"<HASHTAG>\"")

if __name__ == '__main__':
    set_led(0)
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=[hashtag])
    
  
#todo: error handling?
#todo: allow to fail gracefully if we attempt to read from a nonexistant queue?
    
    
    
