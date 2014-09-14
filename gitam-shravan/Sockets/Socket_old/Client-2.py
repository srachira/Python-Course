__author__ = 'SuSh'
import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=socket.gethostname()
port=12345
size=1024
s.connect((host,port))

data = s.recv(size)
s.close()
print 'Received from 12345:', data