

import socket
from deserialization import *

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=socket.gethostname()
port=12347
backlog=5
size=1024
s.bind((host,port))
s.listen(backlog)
print "Waiting for connection on port 12345"

while 1:
    client, address = s.accept()
    print "I got a connection from ", address
    data = client.recv(size)
    print data,"yes 19 server"
    data=deserialization(data)
    print "yes 21 server"
    client.send(str(data))
    print "Sent"
