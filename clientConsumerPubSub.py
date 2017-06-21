from comunication.consumerComunication import ConsumerComunication


def client():
    producer = ConsumerComunication(ConsumerComunication.PUBSUB, 'localhost')
    queue = input("Choose the comunication queue: ")
    producer.receive(queue)


if __name__ == '__main__':
    client()
