__author__ = 'amani'

import socket

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
port=8965
s.connect((host,port))
while True:
    msg=raw_input("enter message")
    s.send(msg)
    print s.recieve()
s.close()
