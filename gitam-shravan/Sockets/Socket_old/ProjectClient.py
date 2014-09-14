import socket
from deserialization import *
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=socket.gethostname()
port=12347
size=1024
s.connect((host,port))

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
    input1=serialization(obj)
    return input1


while 1:
    a=raw_input("Enter:")
    client_input=convert_obj(a)
    s.send(str(client_input))

    print 'sending input:',str(client_input)

    data = s.recv(size)
    print data,"yes 30 client"
    if ( a == 'exit'):
        s.send(a)
        print "Closed"
        s.close()
        break
    print 'Received from 12345:', data

