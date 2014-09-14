__author__ = 'SuSh'
import socket
from deserialization import *
from deserializer import *

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=socket.gethostname()
port=12347
backlog=5
size=1024
s.bind((host,port))
s.listen(backlog)
print "Waiting for connection on port 12345"

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

while 1:
    obj=json()
    client, address = s.accept()
    print "I got a connection from ", address
    data = client.recv(size)
    if data == 'exit':
        client.send(data)
        s.close()

    print data,"yes 37 server"
    data=convert_to_json_object(data)
    print data

    print "yes 39 server"
    client.send(str(data))
    print data
    print "Sent 41"
