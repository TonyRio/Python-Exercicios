#!\usr\bin\python

import socket

sock = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)

host = "192.168.0.2"

port = 443

def portscanner(port):
        if sock.connect_ex((host,port)):
                print ("a porta %d está fechada ! " % (port))
        else:
                print ("a porta %d está aberta ! "  % (port))
portscanner(port)

