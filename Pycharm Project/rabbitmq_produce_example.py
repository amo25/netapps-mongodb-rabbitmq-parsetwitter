#Produce example:
    #Place: Library
    #Subject: Wishes
    #Message: "I wish I remembered their name"

import pika

#establish a connection with the rabbitmq server, connect a broker on localhost
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange=Place,
                         exchange_type='direct')

channel.basic_publish(exchange=Place,
                      routing_key=Subject,
                      body=Message)

connection.close()