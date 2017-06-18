from abc import ABC, abstractmethod


class ProducerStrategy(ABC):
    """
    Interface to standardize the different strategies of the comunication
    between consume and producer.
    """

    @abstractmethod
    def send(self, message, name):
        pass
