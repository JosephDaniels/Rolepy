##Pychat version 0.1
##Made in 2012
##Written by Jordan Vo

##Made using the documentation:
#http://docs.python.org/howto/sockets.html
#

users = {}

from socket import *
from time import time, ctime

IP = ''
PORT = 23456
ADS = (IP, PORT)

tcpsoc = socket(AF_INET, SOCK_STREAM)
tcpsoc.bind(ADS)
tcpsoc.listen(5)

print "Waiting for connection"
tcpcli, addr = tcpsoc.accept()
print "connected from:", addr
while True:
    data = tcpcli.recv(1024)
    if not data:
        break
    print data
    data1 = raw_input(">>")
    if data1 == "quit":
        break
    tcpcli.send(data1)
    
tcpcli.close()
tcpsoc.close()
