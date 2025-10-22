import socket

HOST = ''              # Endereco IP do Servidor
PORT = 5300            # Porta que o Servidor ouvirá
orig = (HOST, PORT)

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.bind(orig)
tcp.listen(1)

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
    con, cliente = tcp.accept()
    print("Conectado com %s" % str(cliente))

    while True:
        msg = con.recv(1024)
        if not msg:
            break
        print(cliente, str(msg, encoding='utf-8'))
        
        try:
            palavra, idioma = str(msg, encoding='utf-8').split(':')
        except ValueError:
            palavra, idioma = None, None
        resposta = "SERVER SIDE: Palavra nao encontrada.\nO formato da mensagem deve ser 'palavra:en/es'.\nAs palavras disponiveis são: " + ', '.join(palavras.keys())
        
        if palavra in palavras and idioma in palavras[palavra]:
            resposta = "SERVER SIDE: " + palavras[palavra][idioma]
            
        con.send(resposta.encode('utf-8'))

    print(str.format("Finalizando conexao do cliente {}", cliente))

    con.close()