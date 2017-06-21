from abc import ABC, abstractmethod


class ProducerStrategy(ABC):
    """
    Interface to standardize the different strategies of the comunication
    between consume and producer.
    """

    def __init__(self, channel):
        """
        ProducerStrategy class constructor
        """

        self.channel = channel

    @abstractmethod
    def send(self, message, queue):
        """
        Send a single message to the queue.

        @Param message: Message that will be sent to the queue
        @Param queue: Name of the specific queue that the message should go.

        Return: Nothing
        """

        pass
