from comunication.consumer.consumerStrategy import ConsumerStrategy


class Simple(ConsumerStrategy):
    """
    This class will receive messages from the queue and print them on the
    screen.
    """

    def receive(self, queue):
        """
        Receive messages from the queue and print them on the screen.

        @Param name: Name of the specific queue that the message comes.

        Return: Nothing
        """

        self.__create_queue(queue)
        self.callback_consume(queue)

        print(' [*] Waiting for messages. To exit press CTRL+C')

        self.wait_for_data()

    def __create_queue(self, queue):
        """
        Before receive we need to make sure the recipient queue exists.
        Create a queue to get message.

        @Param queue: Queue specifies where the message will be delivered.

        Return: Nothing.
        """

        self.channel.queue_declare(queue=queue)
