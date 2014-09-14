__author__ = 'SuSh'
import socket
from deserialization import *


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
def convert_obj(a):
    global dict
    a=a.split(' ')
    if a[0] in dict['request_type']:
        request_type=a[0]
    else:
        print"Enter a valid Command"
    forum_name=a[1]
    msg=a[2:]
    obj=json(request_type,forum_name,msg)
    input1=obj1.serialization(obj)
    return input1

s=mysocket()
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=socket.gethostname()
port=12347
size=1024
s.connect((host,port))
while 1:
    obj1=json()
    a=raw_input("Enter:")
    client_input=convert_obj(a)
    s.send(str(client_input))
    print "49"
    print 'sending input:',str(client_input)
    print "51"
    data = s.recv(size)
    print data,"yes 30 client"
    if ( a == 'exit'):
        s.send(a)
        print "Closed"
        s.close()
        break
    print 'Received from 12345:', data

