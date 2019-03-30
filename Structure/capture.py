#Filename: repository.py
#Description: client
#ECE 4564 - Assignment 2
#Team 19 : Alexander Orlov, Maura Hartmann, Mark Owen

# DEPENDENCIES
import RPi.GPIO as GPIO
import time

# TODO:
#import Tweepy                       # for twitter
#import pymongo                      # for nosql
#from pymongo import MongoClient
import pika                         # for rabbitmq
#import captureKeys

RED = 21
GREEN = 22
BLUE = 23

# GPIO
def setGPIO():
    channels=[RED, GREEN, BLUE]
    GPIO.setup(channels, GPIO.OUT, initial=GPIO.LOW)

# LED STATUS
def status(number):
    # white = waiting for a command
    if number == 0:
        GPIO.output(RED, GPIO.LOW)
        GPIO.output(GREEN, GPIO.LOW)
        GPIO.output(BLUE, GPIO.LOW)
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

# TODO: SET UP TWITTER
# key/token authorization stuffs
def setTwitter():
    print("TODO")
# TODO : SET UP MONGO - NOSQL
# mongo client stuffs to connect mongoDB
# I think this is where you would put the message command in MongoDB datastore? idk
def setNOSQL():
    print("TODO")

#Rabbit MQ
#Prerequisite: exchanges, bindings, and queue's must be set up
#Another function can be made for this, or we can use the web based gui
def produce(Place, Subject, Message):
    credentials = pika.PlainCredentials('Alex', 'MarioBaseball2572')
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', credentials=credentials)) #todo modify to connect pi's
    channel = connection.channel()

    channel.basic_publish(
        exchange=Place, routing_key=Subject, body=Message)
    print(" [x] Sent %r:%r" % (Subject, Message))
    connection.close()
    
def consume(Place, Subject):
    credentials = pika.PlainCredentials('Alex', 'MarioBaseball2572')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', credentials=credentials)) #todo replace with ip
    channel = connection.channel()
    #get all available messages then quit
    while(True):
        (method, properties, body) = channel.basic_get(queue=Subject, auto_ack=True)
        if (method == None):
            break
        else:
            print("%r:%r" % (method.routing_key, body))
    
# TODO : SOME FUNCTION TO PROCESS TWEET
# splits to get Action, Place, MSGID, Subject, Message
# return produce / consume message request

# TODO : SOME MAIN
# some loop to continuously check/process tweets
# /update led/messssage stuff/wait for response
# print the message command sent
while (True) :
    produce('Library', 'Noise', 'Its ok. Medium volume')
    produce('Library', 'Noise', 'Its probably quiet on fourth')
    consume('Library', 'Noise')
    
