from comunication.producer.producerStrategy import ProducerStrategy


class Simple(ProducerStrategy):
    """
    This class will send a single message to the queue.
    """

    def send(self, message, queue):
        """
        Send a single message to the queue.

        @Param message: Message that will be sent to the queue
        @Param queue: Name of the specific queue that the message should go.

        Return: Nothing
        """

        self.__create_queue(queue)
        self.__queue_exchange(queue, message)

    def __create_queue(self, queue):
        """
        Before sending we need to make sure the recipient queue exists.
        Create a queue to which the message will be delivered

        @Param queue: Especific queue that the message should go.

        Return: Nothing
        """

        self.channel.queue_declare(queue=queue)

    def __queue_exchange(self, queue, message):
        """
        In RabbitMQ a message can never be sent directly to the queue, it always
        needs to go through an exchange. This exchange allows us to specify
        exactly to which queue the message should go.

        @Param queue: Especific queue that the message should go.
        @Param message: Message that will be sent to the queue

        Return: Nothing.
        """

        self.channel.basic_publish(exchange='',
                                   routing_key=queue,
                                   body=message)

        print(" [x] Simple sent %r" % message)
