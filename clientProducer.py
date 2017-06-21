from comunication.producerComunication import ProducerComunication
from comunication.connection import ConnectionRabbitMQ


def client():
    run = True
    option = 'S'

    connection = ConnectionRabbitMQ('localhost')
    channel = connection.get_channel()
    producer1 = ProducerComunication(ProducerComunication.SIMPLE, channel)
    producer2 = ProducerComunication(ProducerComunication.PUBSUB, channel)

    while(run):
        message = input("Insert the message: ")
        queue = input("Choose the communication queue: ")
        producer1.send(message, queue)
        producer2.send(message, queue)

        option = input("Would you like to insert another message? (S/N): ")
        if option.upper() == 'N':
            connection.close()
            run = False

if __name__ == '__main__':
    client()
