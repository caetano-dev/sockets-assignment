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
    'conexao': {'en': 'connection', 'es': 'conexion'},
    'congestionamento': {'en': 'congestion', 'es': 'congestion'},
    'pacote': {'en': 'packet', 'es': 'paquete'},
    'latencia': {'en': 'latency', 'es': 'latencia'},
    'propagacao': {'en': 'propagation', 'es': 'propagacion'},
    'privacidade': {'en': 'privacy', 'es': 'privacidad'},
    'criptografia': {'en': 'encryption', 'es': 'cifrado'}
}

def listar_palavras():
    return ', '.join(palavras.keys())

while True:
    message, clientAddress = udp.recvfrom(2048)
    print(message, clientAddress)
    try:
        palavra, idioma = str(message, encoding='utf-8').split(':', 1)
    except ValueError:
        palavra, idioma = None, None

    resposta = (
        "Palavra nao encontrada. "
        "O formato da mensagem deve ser 'palavra:en/es'. "
        "As palavras disponiveis sao: " + listar_palavras()
    )

    if palavra in palavras and idioma in palavras[palavra]:
        resposta = palavras[palavra][idioma]

    udp.sendto(resposta.encode('utf-8'), clientAddress)

udp.close()