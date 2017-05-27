# Networking Project 2
# Client in Python using 2.7.5

import socket
import sys
import signal
import os


######################################
# Function to verify command line arguments
# verify that there are 5 arguments and that usage is correct
# else print usage to user and exit
def verifyNumArguments():
  if len(sys.argv) != 5:
    print "Usage: ftclient flip1 30021 -l 30020"
    exit(1)



# Verify user entered correct number of arguments
verifyNumArguments() 






s = socket.socket()
host = socket.gethostname()
#port = 50050


# Client usage  ftclient flip1 30021 -l  30021
port = int(sys.argv[2])



s.connect((host,port))
print s.recv(1024)



#close the connection
s.close
print "hello"
