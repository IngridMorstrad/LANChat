# TCP client example
import socket, msvcrt
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("172.16.14.83", 5000))
#client_socket.connect(("localhost", 5000))
data='start'
data2=olddata='start'
client_socket.setblocking(0)

while 1:
    if msvcrt.kbhit() and msvcrt.getch() == chr(99).encode():
        data2= raw_input ( "SEND( TYPE q or Q to Quit):" )
    try:
        data = client_socket.recv(512)
    except:
        pass
    if ( data == 'q' or data == 'Q'):
        client_socket.close()
        data=olddata
        break;
    if data<>olddata:
        print "RECEIVED: " , data
        olddata=data
    if (data2 <> 'Q' and data2 <> 'q'):
        if data2<>olddata:
            client_socket.send(data2)
        elif data2<>olddata:
            client_socket.send(data2)
            client_socket.close()
            break;
    olddata=data=data2
            
