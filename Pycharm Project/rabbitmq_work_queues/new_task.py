import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#todo figure out if this queue sticking around is a problem. Sticks around even if RPi restarts
channel.queue_declare(queue='task_queue', durable=True) #durable means that task_queue won't be lost, even if rabbitmq restarts

message = ' '.join(sys.argv[1:]) or "Hello World!" #add capability to add an arbitrary message
channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=2,  # make message persistent
    ))
print(" [x] Sent %r" % message)
connection.close()