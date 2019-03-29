#a sample worker task
#it does fake work based on the number of "." in a received message

import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.')) #simulates work. Two ".." in a received message = 2 second delay
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag) #in basic_consume, we have manual acknowledgement set, so we must acknowledge when we're done. (no_ack is not set to true, so set to false by defualt)


channel.basic_qos(prefetch_count=1) #don't dispatch a message until the worker has acknowledged the previous one (so we'll finish processing the previous one before accepting a new one)
channel.basic_consume(queue='task_queue', on_message_callback=callback)

channel.start_consuming()