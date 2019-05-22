##Pychat version 0.1
##Made in 2012
##Last updated 2019
##Written by Jordan Vo

##This program is FREEWARE; feel free to use and redistribute and/or modify it
##as you please. I made this program in hopes of understanding the python module
##SOCKETS and I hope it can help you too.

##This program is provided without warranty
##or even any guarantee that it will work at all.

##That being said, let's check it out!

from socket import *

IP = '127.0.0.1'
PORT = 23456
ADS = (IP, PORT)

tcp_socket = socket(AF_INET, SOCK_STREAM)
tcpsoc.connect(ADS)

while True:
    data = raw_input("msg>>")
    if not data : break
    tcpsoc.send(data)
    data = tcp_socket.recv(1024)
    if not data: break
    print data
    tcpsoc.close()
