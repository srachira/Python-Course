__author__ = 'SuSh'
import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=socket.gethostname()
port=12345
backlog=5
size=1024
s.bind((host,port))
s.listen(backlog)
print "Waiting for connection on port 12345"
while 1:
    client1, address1 = s.accept()

    data = client1.recv(size)
    client2, address2 = s.accept()
    print
    if data:
        client2.send(data)
    client1.close()
    client2.close()