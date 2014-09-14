__author__ = 'amani'

import socket
import json
import data_store

class mysocket:
    def __init__(self,sock=None):
        if sock is None:
            self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
        else:
            self.sock=sock

    def connect(self,(host,port)):
        self.sock.connect((host,port))

    def send(self,msg):
        sent = self.sock.send(msg)
        if sent==0:
            print "Runtime error"

    def recieve(self):
        return  self.sock.recv(1024)

    def close(self):
        self.sock.close()

s=mysocket()
host=socket.gethostname()
port=8999
s.connect((host,port))
while True:
    msg=raw_input(">> ")
    #length=len(msg)
    #print length
    #s.send(str(length))
    #print s.recieve()
    #s.send(msg)

    client_json=json.json()
    client_json.deserializer(msg)
    s.send(client_json.representation())
    #s.send(str(client_json.deserializer(msg)))
    print "sent"
    print "1"
    received= s.recieve()
    print "2"
    print received
    print "3"
    #recd_msg=client_json.serializer(received)
    #print recd_msg
s.close()