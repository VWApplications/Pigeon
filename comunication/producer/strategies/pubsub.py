from comunication.producer.producerStrategy import ProducerStrategy


class PubSub(ProducerStrategy):
    """
    Simple system that emit messages In our system every running copy of the
    receiver program will get the messages.

    Essentially, published messages are going to be broadcast to all the
    receivers.

    We'll deliver a message to multiple consumers.
    This pattern is known as "publish/subscribe".
    """

    def send(self, message, queue):
        """
        Deliver a message

        @Param message: Message that will be published
        @Param queue: Name of the exchange of type fanout

        Return: Nothing
        """

        self.__fanout_exchange_type_declare(queue)
        self.__publish_exchange(queue, message)

    def __fanout_exchange_type_declare(self, exchange):
        # Declare an exchange of type fanout that send messages to an exchange and
        # the exchange must know exactly what to do with a message it receives
        # On one side it receives messages from producers and the other side it
        # pushes them to queues.
        # The rules for that are defined by the exchange type (fanout) it just
        # broadcasts all the messages it receives to all the queues it knows.

        self.channel.exchange_declare(exchange=exchange, type='fanout')

    def __publish_exchange(self, exchange, message):
        # Creates an exchange without a defined queue and insert a message on it
        # and print the message

        self.channel.basic_publish(exchange=exchange,
                                   routing_key='',
                                   body=message)

        print(" [x] PubSub sent %r" % message)
