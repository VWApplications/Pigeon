# PyPigeon

Pigeon in python

RabbitMQ is a message broker: it accepts and forwards messages. You can
think about it as a post office: when you put the mail that you want posting
in a post box, you can be sure that Mr. Postman will eventually deliver the
mail to your recipient.In this analogy, RabbitMQ is a post box, a post
office and a postman.

A producer is a user application that sends messages.
A queue is a buffer that stores messages.
A consumer is a user application that receives messages.


***
### How to test it
***

This test assumes that RabbitMQ is installed and running on localhost on standard port (5672).

1. Open two control terminals and run one client at each terminal

    - **clientConsumer** will get messages from **clientProducer**

    - **clientProducer**: will insert messages to be consumed

2. Insert the comunication queue on **clientConsumer** first

3. Then, insert the message on **clientProducer** and the comunication queue that will be showing on Consumers

* **Obs**: If you want to change the connection type, in the client files change from SIMPLE to the other one you want

  - SIMPLE
  - PUBSUB
  - ...

***
#### References
***

* **RabbitMQ**: https://www.rabbitmq.com/
