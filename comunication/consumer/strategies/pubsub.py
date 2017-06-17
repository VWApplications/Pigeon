from comunication.consumer.consumerStrategy import ConsumerStrategy
from comunication.connection import ConnectionRabbitMQ
import sys  # Provides access to some variables used by the interpreter


class PubSub(ConsumerStrategy):
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

    def send(self, message, name):
        """
        Deliver a message

        Parameters:

            - message: Message that will be published
            - name: Name of the exchange of type fanout

        Return: Nothing
        """

        connection = self.rabbitMQ.establish_connection()
        channel = self.rabbitMQ.create_channel(connection)
        self.fanout_exchange_type_declare(channel, name)
        message = self.create_message()
        self.publish_exchange_name(channel, name, message)
        self.rabbitMQ.close_connection(connection)

    def fanout_exchange_type_declare(channel, exchange_name):
        """
        Declare an exchange of type fanout that send messages to an exchange and
        the exchange must know exactly what to do with a message it receives

        On one side it receives messages from producers and the other side it
        pushes them to queues.

        The rules for that are defined by the exchange type (fanout) it just
        broadcasts all the messages it receives to all the queues it knows.

        Parameters:

            - channel: The channel connection.
            - exchange_name: Name of the exchange of type fanout

        Return: Nothing
        """

        channel.exchange_declare(exchange=exchange_name, type='fanout')

    def create_message():
        """
        Create a message that will be send.

        Return: Message
        """

        message = ' '.join(sys.argv[1:]) or "info: Hello World!"
        return message

    def publish_exchange_name(channel, exchange_name, message):
        """
        Creates an exchange without a defined queue and insert a message on it
        and print the message

        Parameters:

            - channel: The channel connection
            - exchange_name: Name of exchange
            - message: Message that will be published

        Return: Nothing
        """

        channel.basic_publish(exchange=exchange_name,
                              routing_key='',
                              body=message)

        print(" [x] Sent %r" % message)
