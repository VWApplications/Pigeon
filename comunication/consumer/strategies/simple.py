from comunication.consumer.consumerStrategy import ConsumerStrategy
from comunication.connection import ConnectionRabbitMQ


class Simple(ConsumerStrategy):
    """
    This class will receive messages from the queue and print them on the
    screen.
    """

    def __init__(self):
        """
        Simple class constructor
        """

        self.rabbitMQ = ConnectionRabbitMQ()

    def receive(self, queue):
        """
        Receive messages from the queue and print them on the screen.

        Parameters:

            - name: Name of the specific queue that the message comes.
        """

        connection = self.rabbitMQ.establish_connection()
        channel = self.rabbitMQ.create_channel(connection)
        self.create_queue(channel, queue)
        self.rabbitMQ.callback_consume(channel, queue)

        print(' [*] Waiting for messages. To exit press CTRL+C')

        self.rabbitMQ.wait_for_data(channel)

    def create_queue(self, channel, queue):
        """
        Before receive we need to make sure the recipient queue exists.
        Create a queue to get message.

        Parameters:

            - channel: The channel conection with the RabbitMQ server.
            - queue: Queue specifies where the message will be delivered.

        Return: Nothing.
        """

        channel.queue_declare(queue=queue)
