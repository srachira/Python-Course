__author__ = 'amani'

import socket
import re
import json
import data_store

class my_serv_socket:
    def __init__(self,sock=None):
        if sock is None:
            self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
        else:
            self.sock=sock

    def bind(self,(host,port)):
        self.sock.bind((host,port))

    def listen(self,num):
        self.sock.listen(num)

    def accept(self):
        return self.sock.accept()

    def send(self,msg):
        self.sock.send(msg)

serv=my_serv_socket()
host=socket.gethostname()
port=8999
serv.bind((host,port))
serv.listen(5)
c,addr=serv.accept()
print "got req from",addr
msg=""
while True:
    #length=c.recv(1024)
    #c.send("got length")
    #msg_len=int(length)+50
    msg=c.recv(1024)
    print msg
    if msg=="exit":
        exit(0)
    else:
        serv_json=json.json()
        print "4"
        out=serv_json.serializer(msg)

        print "5"
        c.send(str(out))
c.close()