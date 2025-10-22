import socket

HOST = ''              # Endereco IP do Servidor
PORT = 5300            # Porta que o Servidor esta

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

orig = (HOST, PORT)

udp.bind(orig)

palavras = {
    'rede': {'en': 'network', 'es': 'red'},
    'roteador': {'en': 'router', 'es': 'enrutador'},
    'comutador': {'en': 'switch', 'es': 'conmutador'},
    'conexão': {'en': 'connection', 'es': 'conexión'},
    'congestionamento': {'en': 'congestion', 'es': 'congestión'},
    'pacote': {'en': 'packet', 'es': 'paquete'},
    'latência': {'en': 'latency', 'es': 'latencia'},
    'propagação': {'en': 'propagation', 'es': 'propagación'},
    'privacidade': {'en': 'privacy', 'es': 'privacidad'},
    'criptografia': {'en': 'encryption', 'es': 'cifrado'}
}

while True:
    message, clientAddress = udp.recvfrom(2048)
    print(message, clientAddress)
    try:
        palavra, idioma = str(message, encoding='utf-8').split(':', 1)
    except ValueError:
        palavra, idioma = None, None

    resposta = "Palavra nao encontrada.\nO formato da mensagem deve ser 'palavra:en/es'.\nAs palavras disponiveis são: " + ', '.join(palavras.keys())

    if palavra in palavras and idioma in palavras[palavra]:
        resposta = palavras[palavra][idioma]

    udp.sendto(resposta.encode('utf-8'), clientAddress)

udp.close()