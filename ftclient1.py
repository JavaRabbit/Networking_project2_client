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



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
#port = 50050


# Client usage  ftclient flip1 30021 -l  30021
port = int(sys.argv[2])



s.connect((host,port))

# Client will first send to server
response = "foobar blah some client command"
s.send(response)

# Save incoming response
# recv can be made to wait for an amount of data
# or until a timeout

# the new file name will be the argument in the command line
target = open(sys.argv[4], "w")
data =  s.recv(1024)

# if the 3rd argument is -g, then save to file
# else if -l, then print to user
if sys.argv[3] == "-g":
  target.write(data)
else:
   print data

# close the file
target.close()

#close the connection
s.close
# print "hello"
