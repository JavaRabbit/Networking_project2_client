#!/bin/python

# Project: Networking Project 2
# Program: FTP Client 
# Language: Python 2.7.5
# Author: Bonnie Kwong
# Description: a python FTP client
# Date: June 1, 2017


import socket
import sys
import signal
import os


######################################
# Function to verify command line arguments
# verify that there are 5 or 6arguments and that usage is correct
# else print usage to user and exit
def verifyNumArguments():
  if (len(sys.argv) != 6 and len(sys.argv) !=5 ) or  (sys.argv[3] != "-g" and sys.argv[3] != "-l"):
    print "Usage: ftclient flip1 30021 -l someFile.txt 30020"
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
response = "foo bar"

# join the list of sys.argv into string
# to send to server
s.send(" ".join(sys.argv[0:]))

# Save incoming response
# recv can be made to wait for an amount of data
# or until a timeout

# variable to receive the data
data =  s.recv(1024) # size

# if the 3rd argument is -g, then save to file
# else if -l, then print to user
if sys.argv[3] == "-g":

  # if the data returned by server
  # is "not found" print this to user instead
  # of putting into text file
  if(data == "not found^@"):
    print sys.argv[1] +":" +  sys.argv[2] + " says FILE NOT FOUND"
    sys.exit()
  target = open(sys.argv[4], "w")
  target.write(data)
  #dat = s.recv(3)  #  size
  #target.write(dat)
  target.close()
else:   # -l  will print data
   print data

# close the file








