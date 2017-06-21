from comunication.consumer.strategies.simple import Simple
from comunication.consumer.strategies.pubsub import PubSub
from comunication.connection import ConnectionRabbitMQ


class ConsumerComunication(object):
    """
    Maintains a reference to a Strategia object and can allow it to access your
    data.
    """

    SIMPLE = 0
    PUBSUB = 1
    strategy = None

    def __init__(self, comunication, ip_address):
        """
        ProducerComunication constructor

        @Param comunication: Comunication type
        @Param ip_address: IP of comunication
        """

        rabbitMQ = ConnectionRabbitMQ(ip_address)
        channel = rabbitMQ.get_channel()
        self.__create_comunication(comunication, channel)

    def __create_comunication(self, comunication, channel):
        """
        Create comunication type

        @Param comunication: Comunication type
        @Param channel: The channel conection with the RabbitMQ server.
        """

        if comunication == self.SIMPLE:
            self.strategy = Simple(channel)
        elif comunication == self.PUBSUB:
            self.strategy = PubSub(channel)
        else:
            raise NameError('Communication type not found')

    def receive(self, queue):
        """
        Receive and print messages.

        @Param queue: Name of the exchange of type fanout

        Return: Nothing
        """

        self.strategy.receive(queue)
