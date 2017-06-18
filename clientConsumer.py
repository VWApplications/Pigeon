from comunication.consumerComunication import ConsumerComunication


def client():
    run = True
    option = 'S'
    consumer1 = ConsumerComunication(ConsumerComunication.SIMPLE)
    consumer2 = ConsumerComunication(ConsumerComunication.PUBSUB)

    print("Comunicação Simple")

    while(run):
        message = input("Insert the message: ")
        queue = input("Choose the communication queue: ")
        consumer1.send(message, queue)
        consumer2.send(message, queue)

        option = input("Would you like to insert another message? (S/N): ")
        if option.upper() == 'N':
            run = False

if __name__ == '__main__':
    client()
