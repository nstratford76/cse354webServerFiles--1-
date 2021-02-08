#############################################################################
# Program:
#    Lab PythonWebServer, Computer Networks
#    Brother Jones, CSE354
# Author:
#    Nathan Stratford
# Summary:
#    This progam ...
#
##############################################################################

#
from socket import *
import sys
import os

# Return proper content type
def contentType(filepath):
   # Based on the file extension, return the content type 
   # that is part  of the "Content-type:" header"

   return 

# Server Connection Setup
serverPort = int(sys.argv[1]) if len(sys.argv) == 2 else 6789
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print ("Server is running on port " , str(serverPort))

CRLF = "\r\n"
try:
   # Main Server Loop
   while 1:
      # Things to be done include:
      #  -accept a connection
      connectionSocket, addr = serverSocket.accept()
      #  -read the request (if an empty request ignore it)
      message = connectionSocket.recv(1024).decode()
      filename = message.split()[1]
      if os.path.isfile(filename): 
         f = open(filename[1:])
         outputdata = f.read()
         f.close()
         connectionSocket.send(b'HTTP/1.1 200 OK\r\n\r\n')
         for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
         connectionSocket.close()
      else:
         errorPage = "/404.html"
         f = open(errorPage[1:])
         output = f.read()
         f.close()
         connectionSocket.send(b'HTTP/1.1 404 NOT FOUND\r\n\r\n')
         for i in range(0, len(errorPage)):
            connectionSocket.send(errorPage[i].encode())
         connectionSocket.close()
      #  -parse token from the request string
      #  -make sure the file exists
      #     -all files are to be relative to the directory 
      #      in which the web server was started
      
      #  -create and send the status line
      #  -create and send the "Content-type:" header
      #  -What goes between the header lines and the requested file?
      #  -send the file or 404 message
      
      #     -open a file in binary like ... = open(filepath, "rb")
     
      #  -don't forget to close the connection socket


except KeyboardInterrupt:
   print ("\nClosing Server")
   serverSocket.close()
   quit()
