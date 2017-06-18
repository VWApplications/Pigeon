from comunication.producer.producerStrategy import ProducerStrategy
from comunication.connection import ConnectionRabbitMQ


class Simple(ProducerStrategy):
    """
    This class will send a single message to the queue.
    """

    def __init__(self):
        """
        Simple class constructor
        """

        self.rabbitMQ = ConnectionRabbitMQ()

    def send(self, message, queue):
        """
        Send a single message to the queue.

        Parameters:

            - message: Message that will be sent to the queue
            - queue: Name of the specific queue that the message should go.

        Return: Nothing
        """

        connection = self.rabbitMQ.establish_connection()
        channel = self.rabbitMQ.create_channel(connection)
        self.__create_queue(channel, queue)
        self.__queue_exchange(channel, queue, message)
        self.rabbitMQ.close_connection(connection)

    def __create_queue(self, channel, queue):
        """
        Before sending we need to make sure the recipient queue exists.
        Create a queue to which the message will be delivered

        Parameters:

            - channel: Communication channel with the RabbitMQ server
            - queue: Especific queue that the message should go.

        Return: Nothing
        """

        channel.queue_declare(queue=queue)

    def __queue_exchange(self, channel, queue, message):
        """
        In RabbitMQ a message can never be sent directly to the queue, it always
        needs to go through an exchange. This exchange allows us to specify
        exactly to which queue the message should go.

        Parameters:

            - channel: Communication channel with the RabbitMQ server
            - queue: Especific queue that the message should go.
            - message: Message that will be sent to the queue

        Return: Nothing.
        """

        channel.basic_publish(exchange='',
                              routing_key=queue,
                              body=message)

        print(" [x] Simple sent %r" % message)
