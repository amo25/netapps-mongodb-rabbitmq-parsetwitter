#TODO just set up a bunch of consumes?
import pika

Place = 'Squires' #todo replace? Put in plaintext into each call, and make calls for all 3 excahanges, and all 8 queues?
Subject = 'Food'

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')) #todo replace with ip
channel = connection.channel()

#Todo can comment back in to ensure that exchange exists
#channel.exchange_declare(exchange=Place, exchange_type='direct')

#result = channel.queue_declare(Subject, exclusive=True) #todo should this be exclusive?

#channel.queue_bind(
    #exchange='direct_logs', queue=Subject, routing_key=)



def callback(ch, method, properties, body):
    print("%r:%r" % (method.routing_key, body))


channel.basic_consume(
    queue=Subject, on_message_callback=callback, auto_ack=True)

channel.start_consuming()

