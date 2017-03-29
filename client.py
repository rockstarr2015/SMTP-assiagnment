#import socket module

from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)

port =  8000

host = 'localhost'

serverSocket.connect((host, port))

print(serverSocket.recv(1024))

serverSocket.close()