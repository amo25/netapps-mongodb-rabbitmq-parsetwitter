# Filename: repository.py
# Description: server
# ECE 4564 - Assignment 2
# Team 19 : Alexander Orlov, Maura Hartmann, Mark Owen

# DEPENDENCIES
#TODO :
import pika

# TODO: CALLBACK FUNCTION
# append message and print the received message command
def callback(ch, method, properties, body):

# TODO: RABBITMQ STUFF
# Manage RabbitMQ messages via direct exchange and queues
# stuffs below from slides
channel.queue_bind(exchange='Place',
                   queue=queue_name,
                   routing_key=Subject)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()