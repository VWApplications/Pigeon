from abc import ABC, abstractmethod


class ProducerStrategy(ABC):
    """
    Interface to standardize the different strategies of the comunication
    between consumer and producer.
    """

    @abstractmethod
    def receive(self, name):
        pass
