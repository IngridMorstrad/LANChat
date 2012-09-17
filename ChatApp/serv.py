# TCP server example
import socket, msvcrt
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(), 5000))
#server_socket.bind(("localhost", 5000))
server_socket.listen(5)

print "TCPServer Waiting for client on port 5000"

while 1:
        client_socket, address = server_socket.accept()                        
        print "I got a connection from ", address
        data='start'
        olddata2='start'
        olddata=olddata2
        client_socket.setblocking(0)
        while 1:
                if (data == 'Q' or data == 'q'):
                        client_socket.send (data)
                        client_socket.close()
                        break;
                else:
                        try:
                                data=client_socket.recv(512)
                                if data!=olddata2:
                                        print "CLIENT: ", data
                                        olddata2=data
                        except:
                                pass
                        if msvcrt.kbhit() and msvcrt.getch() == chr(99):
                                data= raw_input ( "SEND( TYPE q or Q to Quit):" )
                                client_socket.send(data)
                                olddata=data
                        if (data == 'q' or data == 'Q'):
                                client_socket.close()
                                break;
