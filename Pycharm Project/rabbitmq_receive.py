import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

#the callback function to a subscribe to the queue
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

#tell rabbitmq to subscribe particular callback function
channel.basic_consume(
    queue='hello', on_message_callback=callback, auto_ack=True)

#never ending loop which waits for messages
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
