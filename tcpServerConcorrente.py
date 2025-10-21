import socket
import sys
import threading as thread

HOST = ''              # Endereco IP do Servidor
PORT = 5300            # Porta que o Servidor ouvirá
orig = (HOST, PORT)
def conectado(con, cliente):
    print('Conectado por', cliente)

    while True:
        msg = con.recv(1024)
        if not msg: break
        print(cliente, str(msg, encoding = 'utf-8'))
        resposta = "SERVER SIDE: " + str.upper(str(msg, encoding='utf-8'))
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
