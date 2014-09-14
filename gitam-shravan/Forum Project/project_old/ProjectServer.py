__author__ = 'SuSh'
__author__ = 'SuSh'
import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=socket.gethostname()
port=12346
backlog=5
size=1024
s.bind((host,port))
s.listen(backlog)
dict={"algo":["abc","def"],"datastr":["ghi","bcf"]}
print "Waiting for connection on port 12345"

def view(data):
    global dict
    if data=="forum":
        return dict.keys()
    else:
        return dict[data]
def write(key, value):
    global dict
    dict[key].append(value)
    return dict[key]

while 1:
    client, address = s.accept()
    print "I got a connection from ", address
    while 1:
        data = client.recv(size)
        data=data.split(" ")
        if (data == 'Q' or data == 'q'):
            client.send (data)
            client.close()
            break
        if data[0] == "view":
            viewdict= view(data[1])
            client.send(str(viewdict))
        if data[0] == "write":
            k=write(data[1],data[2])
            print k
            client.send(str(k))
        if data == 'q' or data == 'Q':
            client.close()
            break
