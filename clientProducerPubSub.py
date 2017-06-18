from comunication.producerComunication import ProducerComunication


def client():
    producer = ProducerComunication(ProducerComunication.PUBSUB)
    queue = input("Choose the comunication queue: ")
    producer.receive(queue)


if __name__ == '__main__':
    client()
