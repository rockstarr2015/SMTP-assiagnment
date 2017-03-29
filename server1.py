#import socket module

from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)

port =  8000

host = 'localhost'

#Prepare a sever socket
#Fill in start

serverSocket.bind((host, port))

serverSocket.listen(1)

print('The webserver is running on port', port)

print('The server host:', host)
 
#Fill in end

while True:
 #Establish the connection
 print('Ready to serve...')
 connectionSocket, addr = serverSocket.accept()
 print('got connection from ', addr)
 connectionSocket.send(b' you have been connected to server....')
 
 
 try:
  message = connectionSocket.recv(1024)
  filename = message.split()[1]
  f = open(filename[1:])
  outputdata = f.read()
  print(outputdata)
 
 #Send one HTTP header line into socket
 
 
 #Fill in start
  connectionSocket.send('\nHTTP/1.1 200 OK\n\n')
  connectionSocket.send(outputdata)
 
 #Fill in end
 #Send the content of the requested file to the client
  for i in range(0, len(outputdata)):
   connectionSocket.send(outputdata[i])
   connectionSocket.close()
 except IOError:
 #Send response message for file not found
 #Fill in start
  connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n')
  connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n')
 #Fill in end
 #Close client socket
 #Fill in start
  connectionSocket.close()
 #Fill in end 
serverSocket.close() 