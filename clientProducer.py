from comunication.producerComunication import ProducerComunication


def client():
    run = True
    option = 'S'
    producer1 = ProducerComunication(ProducerComunication.SIMPLE)
    producer2 = ProducerComunication(ProducerComunication.PUBSUB)

    while(run):
        message = input("Insert the message: ")
        queue = input("Choose the communication queue: ")
        producer1.send(message, queue)
        producer2.send(message, queue)

        option = input("Would you like to insert another message? (S/N): ")
        if option.upper() == 'N':
            run = False

if __name__ == '__main__':
    client()
