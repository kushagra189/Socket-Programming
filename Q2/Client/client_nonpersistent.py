import socket
import time
import sys
import os

num = int(raw_input("Enter No. of files"))
files = []

for i in range(num):
    file = raw_input("Enter file to get:")
    files.append(file)

start_t = time.time()

for filename in files:

    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    host = ""
    port = 60001
    try:
        s.connect((host, port))
        if not filename:
            print("Connected")
    except:
        print("Error connecting")
        sys.exit()
    try:
        s.send(filename)
    except:
        print("sending error")
        sys.exit()

    filename = filename.split('/')
    p = len(filename) - 1
    filename = filename[p]
    
    with open(filename, 'wb') as f:
        print 'file opened'
        while True:
            print('receiving data...')
            blocks = s.recv(1024)
            if not blocks:
                print('No such file found')
                os.remove(filename)
                s.close()
                # continue
                sys.exit()

            # print('blocks=%s', (blocks))
            # write blocks to a file
            f.write(blocks)
            if len(blocks)<1024:
                break

    f.close()

    print('Successfully got the file')
    s.close()
    print('Connection closed')

print(time.time() - start_t)
