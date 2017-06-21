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

    def __init__(self, ip_address='localhost'):
        """
        Connect with RabbitMQ server

        @Param ip_address: IP of comunication
        """

        # Establish a connection with RabbitMQ server
        self.connection = pika.BlockingConnection(
                            pika.ConnectionParameters(ip_address)
                          )

        # Creates the communication channel with the RabbitMQ server
        self.channel = self.connection.channel()


    def get_channel(self):
        """
        Get the connection channel

        @Param channel: The channel conection with the RabbitMQ server.

        Return: channel connection
        """

        return self.channel

    def close(self):
        """
        Before exiting the program we need to make sure the network buffers were
        flushed and our message was actually delivered to RabbitMQ. We can do it
        by gently closing the connection

        @Param connection: Parameter that will store the connection

        Return: Nothing
        """

        self.connection.close()
