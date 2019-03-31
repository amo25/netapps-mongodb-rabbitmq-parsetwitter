#consume only receives this if it's set to run first?
#I guess that's ok for this project. Check back to see if this is an issue
import pika
#import sys

credentials = pika.PlainCredentials('Alex', '***REMOVED***')
#parameters = pika.ConnectionParameters(credentials=credentials)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', credentials=credentials)) #todo modify to connect pi's
channel = connection.channel()

Place = 'Squires' #todo replace these with a funciton call that sets them
Subject = 'Food'
Message = "Another one"

#channel.exchange_declare(exchange=Place, exchange_type='direct')

channel.basic_publish(
    exchange=Place, routing_key=Subject, body=Message)
print(" [x] Sent %r:%r" % (Subject, Message))
connection.close()
