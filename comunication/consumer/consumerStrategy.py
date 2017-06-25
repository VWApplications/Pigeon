from abc import ABC, abstractmethod


class ConsumerStrategy(ABC):
    """
    Interface to standardize the different strategies of the comunication
    between consumer and producer.
    """

    def __init__(self, channel):
        """
        ConsumerStrategy class constructor

        @Param channel: The channel conection with the RabbitMQ server.
        """

        self.channel = channel

    @abstractmethod
    def receive(self, name):
        pass

    def callback_consume(self, queue):
        """
        We need to tell RabbitMQ that this particular callback function should
        receive messages from our queue.

        @Param queue: Queue specifies where the message will be consumed.

        Return: Nothing.
        """

        self.channel.basic_consume(self.__callback,
                                   queue=queue,
                                   no_ack=True)

    def wait_for_data(self):
        """
        We enter a never-ending loop that waits for data and runs callbacks
        whenever necessary.

        Return: Nothing.
        """

        self.channel.start_consuming()

    def __callback(self, ch, method, properties, body):
        # It works by subscribing a callback function to a queue.
        # Whenever we receive a message, this callback function is called by the
        # Pika library. In our case this function will print on the screen the
        # contents of the message.

        print(" [x] Received %r" % body)

