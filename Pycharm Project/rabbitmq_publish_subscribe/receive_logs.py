import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

#whenever we connect to Rabbit we need a fresh, empty queue
#create a randomly named queue by giving empty string
#exclusize=True means that the queue will be deleted when the consumer connection is closed
result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

#connect the logs exchange to the queue we just created
channel.queue_bind(exchange='logs', queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r" % body)


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()