from comunication.producerComunication import ProducerComunication


def client():
    producer = ProducerComunication(ProducerComunication.SIMPLE)
    queue = input("Choose the comunication queue: ")
    producer.receive(queue)


if __name__ == '__main__':
    client()
