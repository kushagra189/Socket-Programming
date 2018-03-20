import socket
import sys
import os
import time

# os.system("tput reset")
host = ""
port = 60001

while 1:
    try:
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen(5)
    except socket.error:
        print 'Failed to create socket'
        sys.exit()

    print 'Server listening....'

# while True:
    conn, addr = s.accept()
    print 'Connection with client formed'
    filename = conn.recv(1024)

    if not os.path.isfile(filename):
        print('No such file')
        conn.close()
        s.close()
        sys.exit()
    else:
        f = open(filename,'rb')
        l = f.read(1024)
        while (l):
           conn.send(l)
           # print('Sent ',repr(l))
           l = f.read(1024)
        f.close()
        print('Done sending')
        conn.close()
        s.close()
