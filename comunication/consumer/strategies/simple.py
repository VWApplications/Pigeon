from comunication.consumer.consumerStrategy import ConsumerStrategy
from comunication.connection import ConnectionRabbitMQ


class Simple(ConsumerStrategy):
    """
    This class will send a single message to the queue.
    """

    def __init__(self):
        """
        Simple class constructor
        """

        self.rabbitMQ = ConnectionRabbitMQ()

    def send(self, message, name):
        """
        Send a single message to the queue.

        Parameters:

            - message: Message that will be sent to the queue
            - name: Name of the especific queue that the message should go.

        Return: Nothing
        """

        connection = self.rabbitMQ.establish_connection()
        channel = self.rabbitMQ.create_channel(connection)
        self.create_queue(channel, name)
        self.queue_exchange(channel, name, message)
        self.rabbitMQ.close_connection(connection)

    def create_queue(self, channel, queue):
        """
        Before sending we need to make sure the recipient queue exists.
        Create a queue to which the message will be delivered

        Parameters:

            - channel: The channel conection with the RabbitMQ server
            - queue: Especific queue that the message should go.

        Return: Nothing
        """

        channel.queue_declare(queue=queue)

    def queue_exchange(self, channel, queue, message):
        """
        In RabbitMQ a message can never be sent directly to the queue, it always
        needs to go through an exchange. This exchange allows us to specify
        exactly to which queue the message should go.

        Parameters:

            - channel: The channel conection with the RabbitMQ server.
            - queue: Especific queue that the message should go.
            - message: Message that will be sent to the queue

        Return: Nothing.
        """

        channel.basic_publish(exchange='',
                              routing_key=queue,
                              body=message)

        print(" [x] Sent %r" % message)
