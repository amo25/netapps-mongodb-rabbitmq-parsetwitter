import pika


#the callback function to a subscribe to the queue
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello') #Make sure queue exists - queue_declare is idempotent, so we can run it as many times as we like and only one hello queue will be created

#tell rabbitmq to subscribe particular callback function to hello queue
channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

#never ending loop which waits for messages
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

#to list queue's, on the pi run sudo rabbitmqctl list_queues

