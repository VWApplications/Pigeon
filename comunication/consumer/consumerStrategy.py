from abc import ABC, abstractmethod
from comunication.connection import ConnectionRabbitMQ


class ConsumerStrategy(ABC):
    """
    Interface to standardize the different strategies of the comunication
    between consumer and producer.
    """

    def __init__(self):
        """
        ConsumerStrategy class constructor
        """

        self.rabbitMQ = ConnectionRabbitMQ()
        self.connection = self.rabbitMQ.establish_connection()
        self.channel = self.rabbitMQ.create_channel(self.connection)

    @abstractmethod
    def receive(self, name):
        pass

    def __callback(self, ch, method, properties, body):
        """
        It works by subscribing a callback function to a queue.
        Whenever we receive a message, this callback function is called by the
        Pika library. In our case this function will print on the screen the
        contents of the message.

        Return: Nothing.
        """

        print(" [x] Received %r" % body)

    def callback_consume(self, channel, queue):
        """
        We need to tell RabbitMQ that this particular callback function should
        receive messages from our queue.

        Parameters:

            - channel: The channel conection with the RabbitMQ server.
            - queue: Queue specifies where the message will be consumed.

        Return: Nothing.
        """

        channel.basic_consume(self.__callback,
                              queue=queue,
                              no_ack=True)

    def wait_for_data(self, channel):
        """
        We enter a never-ending loop that waits for data and runs callbacks
        whenever necessary.

        Return: Nothing.
        """

        channel.start_consuming()
