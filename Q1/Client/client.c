// Client side C/C++ program to demonstrate Socket programming
#include <stdio.h>
#include <sys/socket.h>
#include <stdlib.h>
#include <netinet/in.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <netdb.h>
#include <ctype.h>
#include <errno.h>
#define PORT 8080

int main(int argc, char const *argv[])
{
    struct sockaddr_in address;
    int sock = 0, valread;
    struct sockaddr_in serv_addr;
    char *hello = "Hello from client";
    char buffer[1024] = {0};

    if(argc<3)
    {
        perror("please check input\n");
        return -1;
    }

    if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0)
    {
        perror("\n Socket creation error \n");
        return -1;
    }

    memset(&serv_addr, '0', sizeof(serv_addr)); // to make sure the struct is empty. Essentially sets sin_zero as 0
                                                // which is meant to be, and rest is defined below

    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(PORT);

    // Converts an IP address in numbers-and-dots notation into either a 
    // struct in_addr or a struct in6_addr depending on whether you specify AF_INET or AF_INET6.
    if(inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr)<=0)
    {
        perror("\nInvalid address/ Address not supported \n");
        return -1;
    }

    if (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0)  // connect to the server address
    {
        perror("\nConnection Failed \n");
        return -1;
    }

    // char buffer[512];
    send(sock,argv[1],1024,0);
    printf("[Client] Receiveing file from Server and saving it as final.txt...");
    char* fr_name = argv[2];
    FILE *fr = fopen(fr_name, "w");
    if(fr == NULL)
        printf("File %s Cannot be opened.\n", fr_name);
    else
    {
        bzero(buffer, 1024); 
        int fr_block_sz = 0;
        while((fr_block_sz = recv(sock, buffer, 1024, 0)) > 0)
        {
            int write_sz = fwrite(buffer, sizeof(char), fr_block_sz, fr);
            if(write_sz < fr_block_sz)
            {
                perror("File write failed.\n");
            }
            bzero(buffer, 1024);
            if (fr_block_sz == 0 || fr_block_sz != 1024) 
            {
                break;
            }
        }
        if(fr_block_sz < 0)
        {
            if (errno == EAGAIN)
            {
                perror("recv() timed out.\n");
            }
            else
            {
                fprintf(stderr, "recv() failed due to errno = %d\n", errno);
            }
        }
        printf("Ok received from server!\n");
        fclose(fr);
    }
    printf("[Client] Connection lost.\n");
    close(sock);
    return 0;
}