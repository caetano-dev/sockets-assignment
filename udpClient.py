import socket

HOST = '127.0.0.1'  # Endereco IP do Servidor
PORT = 5301            # Porta que o Servidor esta

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

destination = (HOST, PORT)

print('Para sair use CTRL+X\n')

msg = bytes(input(), 'utf-8')

while msg != '\x18': # interrompe com CTRL+X
    udp.sendto(msg, destination)
    message, serverAddress = udp.recvfrom(2048)
    print(message, serverAddress)
    msg = bytes(input(), 'utf-8')

udp.close()
