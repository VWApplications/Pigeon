# PyPigeon

Pigeon is a framework developed in python that was made to intermediate the use
of RabbitMQ services in a quick and easy way, these services of communication
between components/services through different types of context of exchange of
messages, being able to be simple, through Publish and subscribe among others,
the framework encapsulates the complexity of communication so that the client
can use it without worrying about its implementation or how it works.

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
