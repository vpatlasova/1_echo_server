import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)
sock.connect(('10.38.165.12', 9090))

#msg = input()
msg = "Hi!"
msg2 = "bye"
client = "dasha"

sock.send(msg.encode())

data = sock.recv(1024)

sock.close()

print(data.decode())
print(client)
