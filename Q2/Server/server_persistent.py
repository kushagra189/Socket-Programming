import socket
import sys
import os

port = 60008
host = ""

try:
    s = socket.socket()
    s.bind((host,port))
    s.listen(5)
except socket.error:
    print 'Failed to create socket'
    sys.exit()

# filename = raw_input("Enter file to share:")
print 'Server listening....'

connection, addr = s.accept()
while True:
    print 'Got connection from', addr
    f_recv = connection.recv(1024)
    # print data
    if not os.path.isfile(f_recv):
        print('No such file')
        connection.close()
        s.close()
        sys.exit()

    else :
        print 'here'
        f = open(f_recv,'rb')
        l = f.read(1024)
        while (l):
            connection.send(l)
            l = f.read(1024)
            f.close()
            print('Done sending')
connection.close()
s.close()
