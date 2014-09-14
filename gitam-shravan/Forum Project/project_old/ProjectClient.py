__author__ = 'SuSh'
import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=socket.gethostname()
port=12346
size=1024
s.connect((host,port))
while 1:
    a=raw_input("Enter:")
    s.send(a)
    data = s.recv(size)
    if ( a== 'q' or a == 'Q'):
        s.send(a)
        print "Closed"
        s.close()
        break
    print 'Received from 12345:', data
