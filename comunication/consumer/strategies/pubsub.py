from comunication.consumer.consumerStrategy import ConsumerStrategy


class PubSub(ConsumerStrategy):
    """
    Simple class that receive messages.
    """

    def receive(self, queue):
        """
        Receive and print messages.

        Parameters:

            - queue: Name of the exchange of type fanout

        Return: Nothing
        """

        self.__fanout_exchange_type_declare(queue)
        temporary_queue = self.__create_temporary_queue()
        self.__binding(queue, temporary_queue)
        self.callback_consume(self.channel, temporary_queue)

        print(' [*] Waiting for messages. To exit press CTRL+C')

        self.wait_for_data(self.channel)

    def __fanout_exchange_type_declare(self, exchange):
        """
        Declare an exchange of type fanout that send messages to an exchange and
        the exchange must know exactly what to do with a message it receives

        On one side it receives messages from producers and the other side it
        pushes them to queues.

        The rules for that are defined by the exchange type (fanout) it just
        broadcasts all the messages it receives to all the queues it knows.

        Parameters:

            - exchange: Name of the exchange of type fanout

        Return: Nothing
        """

        self.channel.exchange_declare(exchange=exchange, type='fanout')

    def __create_temporary_queue(self):
        """
        Hear about all log messages, not just a subset of them, and it is also
        interested only in currently flowing messages not in the old ones.

        Connect to Rabbit we need a fresh, empty queue. To do it we could
        create a queue with a random name

        Once we disconnect the consumer the queue should be deleted.

        Return: The random queue name
        """

        result = self.channel.queue_declare(exclusive=True)
        temporary_queue = result.method.queue
        return temporary_queue

    def __binding(self, exchange, queue):
        """
        Tell the exchange to send messages to our queue. That relationship
        between exchange and a queue is called a binding.
        """

        self.channel.queue_bind(exchange=exchange, queue=queue)
