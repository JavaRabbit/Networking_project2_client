# Networking Project 2
# Client in Python using 2.7.5

import socket

s = socket.socket()
host = socket.gethostname()
port = 50050


s.connect((host,port))
print s.recv(1024)



#close the connection
s.close
print "hello"
