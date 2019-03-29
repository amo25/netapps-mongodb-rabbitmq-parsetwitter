import pika

#establish a connection with the rabbitmq server, connect a broker on localhost
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()

#creates a queue to which message will be delivered, queue named hello
channel.queue_declare(queue='hello')

#send the string "Hello, World" to the hello queue
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')

#print("Hello World")
#print
#" [x] Sent 'Hello World!'"
print(" [x] Sent 'Hello World!'")

#close the connection before exiting
connection.close()