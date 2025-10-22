import socket
import sys
import threading as thread

HOST = ''              # Endereco IP do Servidor
PORT = 5300            # Porta que o Servidor ouvirá
orig = (HOST, PORT)

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

def conectado(con, cliente):
    print('Conectado por', cliente)

    while True:
        msg = con.recv(1024)
        if not msg:
            break

        msg_str = str(msg, encoding='utf-8')
        print(cliente, msg_str)

        try:
            palavra, idioma = msg_str.split(':', 1)
        except ValueError:
            palavra, idioma = None, None

        resposta = "Palavra nao encontrada.\nO formato da mensagem deve ser 'palavra:en/es'.\nAs palavras disponiveis são: " + ', '.join(palavras.keys())

        if palavra in palavras and idioma in palavras[palavra]:
            resposta = palavras[palavra][idioma]

        con.send(resposta.encode('utf-8'))

    print('Finalizando conexao do cliente', cliente)
    con.close()
    sys.exit()

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.bind(orig)
tcp.listen(1) # até 1 conexão pendente

while True:
    con, cliente = tcp.accept()
    clienteThread = thread.Thread(target=conectado, args=(con, cliente))
    clienteThread.start()

tcp.close()