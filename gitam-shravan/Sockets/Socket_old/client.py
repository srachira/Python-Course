__author__ = 'SuSh'
import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=socket.gethostname()
port=12345
size=1024
s.connect((host,port))
s.send('Hello, world\n')
a=[1,2,3]
s.send(str(a))
data = s.recv(size)
s.close()
print 'Received from 12345:', data

s1=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=socket.gethostname()
port=12346
size=1024
s1.connect((host,port))
s1.send("2*4*5/6")
data = s1.recv(size)
s1.close()
print 'Received from 12346:', data



