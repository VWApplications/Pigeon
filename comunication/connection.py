import pika  # Python client recommended by the RabbitMQ


class ConnectionRabbitMQ(object):
    """
    RabbitMQ is a message broker: it accepts and forwards messages. You can
    think about it as a post office: when you put the mail that you want posting
    in a post box, you can be sure that Mr. Postman will eventually deliver the
    mail to your recipient.In this analogy, RabbitMQ is a post box, a post
    office and a postman.

    A producer is a user application that sends messages.
    A queue is a buffer that stores messages.
    A consumer is a user application that receives messages.
    """

    def establish_connection(self):
        """
        Establish a connection with RabbitMQ server

        Return: The connection with RabbitMQ server
        """

        connection = pika.BlockingConnection(
            pika.ConnectionParameters('localhost')
        )
        return connection

    def create_channel(self, connection):
        """
        Creates the communication channel with the RabbitMQ server

        Parameters:

            - connection: Parameter that will store the connection

        Return: The channel connection
        """

        channel = connection.channel()
        return channel

    def close_connection(self, connection):
        """
        Before exiting the program we need to make sure the network buffers were
        flushed and our message was actually delivered to RabbitMQ. We can do it
        by gently closing the connection

        Parameters:

            - connection: Parameter that will store the connection

        Return: Nothing
        """

        connection.close()
