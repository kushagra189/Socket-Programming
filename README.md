# Author :
1. Kushagra Nagori (20161032)
2. Anurag Mehta (20161016)

# Problem Statement :
1. A basic server and client using sockets
2. Persistent and Non Persistent connections

# Directory Structure :
        Q1
            Server
                server.c
                Data
                    Data files
            Client
                client.c

        Q2
            Server
                server.c / server.py
                Data
                    Data files
            Client
                client.c / client.py

## Instructions for question1:
- Untar the file.
- cd 20161032_Assignment1
- cd Q1
- Compile and Run server.c (gcc followed by ./a.out)
- Open another terminal.
- Compile Client.c
- ./a.out "path_of_file_to_be_downloaded" "name_of_new_file_in_which_content_will_be_copied"
- File will be saved.
- connection closes.

# Instructions for question2:
- Untar the file.
- cd 20161032_Assignment1
- cd Q2
  - Persistent
   - cd Server
   - python server.py
   - open new terminal.
   - cd Client
   - python client.py
   - give the file names.
  - Non-Persistent
   - cd Server
   - python server.py
   - open new terminal.
   - cd Client
   - python client.py
   - enter the number of files to be downloaded.
   - give the names of the files.
