__author__ = 'kavya'
import socket
def client():


    s = socket.socket()         # Create a socket object
    host = socket.gethostname() # Get local machine name
    port = 13161         # Reserve a port for your service.

    s.connect((host, port))
    print s.recv(1024)
    assert "Thank you for connecting"
    s.close                     # Close the socket when done
def forum(name,choice):
    li=[]
    li.append(name)
    li.append(choice)
    s=socket.socket()
    host = socket.gethostname()
    port = 13161
    s.connect((host,port))
    s.send(str(li))
    s.close



run = True
while run:
    print "enter the name:"
    name=raw_input()

    print "Choose an option:"
    print "0: create socket"
    print "1: retrieve socket"
    print "2: post a question"
    print "3: exit"
    #print "4: exit"
    choice = raw_input()

    if int(choice)==1:
        name=""


    if int(choice)==3:
            run=False
    forum(name,int(choice))


