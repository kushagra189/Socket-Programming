import socket
import sys
import os
s = socket.socket()
host = ""
port = 60008

s.connect((host, port))
# s.send("Hello server!")
# x = input("no. of files")
while 1:
    f_input = raw_input('enter file name: ')
    s.send(f_input);
    f_input = f_input.split('/')
    k = len(f_input) - 1
    with open(f_input[k], 'wb') as f:
        print 'file opened'
        while True:
            print('receiving data...')
            block = s.recv(1024)
            if not block:
                # s.close()
                print('No such file found')
                os.remove(f_input[k])
                sys.exit()
            # print('block=%s', (block))
            f.write(block)
            if len(block)<1024:
                break
            # write block to a file
    f.close()
    print('Successfully get the file')
s.close()
print('connection closed')
