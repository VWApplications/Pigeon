from comunication.producer.producerStrategy import ProducerStrategy
from comunication.connection import ConnectionRabbitMQ


class PubSub(ProducerStrategy):
    """
    Simple system that emit messages In our system every running copy of the
    receiver program will get the messages.

    Essentially, published messages are going to be broadcast to all the
    receivers.

    We'll deliver a message to multiple consumers.
    This pattern is known as "publish/subscribe".
    """

    def __init__(self):
        """
        PubSub class constructor
        """

        self.rabbitMQ = ConnectionRabbitMQ()

    def send(self, message, queue):
        """
        Deliver a message

        Parameters:

            - message: Message that will be published
            - queue: Name of the exchange of type fanout

        Return: Nothing
        """

        connection = self.rabbitMQ.establish_connection()
        channel = self.rabbitMQ.create_channel(connection)
        self.__fanout_exchange_type_declare(channel, queue)
        self.__publish_exchange(channel, queue, message)
        self.rabbitMQ.close_connection(connection)

    def __fanout_exchange_type_declare(self, channel, exchange):
        """
        Declare an exchange of type fanout that send messages to an exchange and
        the exchange must know exactly what to do with a message it receives

        On one side it receives messages from producers and the other side it
        pushes them to queues.

        The rules for that are defined by the exchange type (fanout) it just
        broadcasts all the messages it receives to all the queues it knows.

        Parameters:

            - channel: Communication channel with the RabbitMQ server
            - exchange: Name of the exchange of type fanout

        Return: Nothing
        """

        channel.exchange_declare(exchange=exchange, type='fanout')

    def __publish_exchange(self, channel, exchange, message):
        """
        Creates an exchange without a defined queue and insert a message on it
        and print the message

        Parameters:

            - channel: Communication channel with the RabbitMQ server
            - exchange: Name of exchange
            - message: Message that will be published

        Return: Nothing
        """

        channel.basic_publish(exchange=exchange,
                              routing_key='',
                              body=message)

        print(" [x] PubSub sent %r" % message)
