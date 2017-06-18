from abc import ABC, abstractmethod


class ConsumerStrategy(ABC):
    """
    Interface to standardize the different strategies of the comunication
    between consumer and producer.
    """

    @abstractmethod
    def receive(self, name):
        pass
