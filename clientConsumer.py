from comunication.consumerComunication import ConsumerComunication


def client():
    consumer = ConsumerComunication(ConsumerComunication.SIMPLE)
    consumer.send('Hello World!', 'hello')
    consumer.send('Teste de mensagem', 'hello')
    consumer.send('Mensagem no log', 'log')


if __name__ == '__main__':
    client()
