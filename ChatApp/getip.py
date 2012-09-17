import socket
print socket.gethostbyname(socket.gethostname())
print socket.gethostbyname_ex(socket.gethostname())
print socket.getfqdn()
print socket.gethostbyname(socket.getfqdn())
