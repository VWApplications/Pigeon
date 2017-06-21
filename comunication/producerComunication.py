from comunication.producer.strategies.simple import Simple
from comunication.producer.strategies.pubsub import PubSub


class ProducerComunication(object):
    """
    Maintains a reference to a Strategia object and can allow it to access your
    data.
    """

    SIMPLE = 0
    PUBSUB = 1
    strategy = None

    def __init__(self, comunication, channel):
        """
        ConsumerComunication constructor that especify the type of comunication

        @Param comunication: Comunication type
        @Param channel: The channel conection with the RabbitMQ server.
        """

        if comunication == self.SIMPLE:
            self.strategy = Simple(channel)
        elif comunication == self.PUBSUB:
            self.strategy = PubSub(channel)
        else:
            raise NameError('Communication type not found')

    def send(self, message, queue):
        """
        Send a single message to the queue.

        @Param message: Message that will be sent to the queue
        @Param queue: Name of the specific queue that the message should go.

        Return: Nothing
        """
        self.strategy.send(message, queue)
