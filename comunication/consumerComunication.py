from comunication.consumer.strategies.simple import Simple
from comunication.consumer.strategies.pubsub import PubSub


class ConsumerComunication(object):
    """
    Maintains a reference to a Strategia object and can allow it to access your
    data.
    """

    SIMPLE = 0
    PUBSUB = 1
    strategy = None

    def __init__(self, comunication):
        """
        ProducerComunication constructor
        """

        if comunication == self.SIMPLE:
            self.strategy = Simple()
        elif comunication == self.PUBSUB:
            self.strategy = PubSub()
        else:
            raise NameError('Communication type not found')

    def receive(self, name):
        self.strategy.receive(name)
