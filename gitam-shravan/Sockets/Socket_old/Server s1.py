
import socket
s1=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=socket.gethostname()
port=12346
backlog=5
size=1024
s1.bind((host,port))
s1.listen(backlog)
print "Waiting for connection on port 123456"
while 1:
    client, address = s1.accept()
    data = client.recv(size)
    if data:
        data=eval(data)
        client.send(str(data))
    client.close()