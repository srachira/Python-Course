__author__ = 'kavya'
import socket
import collections
def server():
    s = socket.socket()         # Create a socket object
    host = socket.gethostname() # Get local machine name
    port = 13162  # Reserve a port for your service.
    s.bind((host, port))        # Bind to the port
    s.listen(5)                 # Now wait for client connection.
    while True:
       c, addr = s.accept()     # Establish connection with client.
       print 'Got connection from', addr
       c.send('Thank you for connecting')
       c.close()                # Close the connection

def main():
        res=[]
        res1=[]
        f_list=[]
        buffer_msg=collections.defaultdict(list)
        s=socket.socket()
        host = socket.gethostname()
        port = 13161
        s.bind((host,port))
        s.listen(5)
        while True:
            c,addr = s.accept()
            res=c.recv(1024)
            res1=res.split(',')
            for each in res1:
                if '[' in each:
                    name= each.strip('[')
                else:
                    choice= each.strip(']')
            if int(choice) == 0:
                forum_creation(f_list,name)
            if int(choice) == 1:
                get_forum(f_list)
            if int(choice) == 2:
                message=c.recv(1024*1024)
                print message
                post_forum(name,message,buffer_msg)

            #print res
        c.close()


def forum_creation(forum_list,res):

        if res in forum_list:
            print "name already exists"
        else:
            forum_list.append(res)
        print forum_list


def get_forum(flist):
    print flist
def post_forum(name,message,buffer_msg):
    buffer_msg[name].append(message)
    print buffer_msg

if __name__=="__main__":
    main()