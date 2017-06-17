from abc import ABC, abstractmethod


class ConsumerStrategy(ABC):
    """
    Interface to standardize the different strategies of the comunication
    between consume and producer.
    """

    @abstractmethod
    def send(self, message, name):
        pass
