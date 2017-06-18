from comunication.consumer.consumerStrategy import ConsumerStrategy


class Simple(ConsumerStrategy):
    """
    This class will receive messages from the queue and print them on the
    screen.
    """

    def receive(self, queue):
        """
        Receive messages from the queue and print them on the screen.

        Parameters:

            - name: Name of the specific queue that the message comes.
        """

        self.__create_queue(queue)
        self.callback_consume(self.channel, queue)

        print(' [*] Waiting for messages. To exit press CTRL+C')

        self.wait_for_data(self.channel)

    def __create_queue(self, queue):
        """
        Before receive we need to make sure the recipient queue exists.
        Create a queue to get message.

        Parameters:

            - channel: The channel conection with the RabbitMQ server.
            - queue: Queue specifies where the message will be delivered.

        Return: Nothing.
        """

        self.channel.queue_declare(queue=queue)
