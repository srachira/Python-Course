__author__ = 'ProfAVR'

import socket
import json
from project13_forums.sockets.server.classes.user import *
from memory import *
from project13_forums.sockets.server.classes.UserAuth import *
from project13_forums.sockets.server.classes.ViewForum import *

class server_socket:
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        else:
            self.sock = sock

    def bind(self, (host, port)):
        self.sock.bind((host, port))

    def listen(self, num):
        self.sock.listen(num)

    def accept(self):
        return self.sock.accept()

    def send(self, msg):
        self.sock.send(msg)


def server():
    serv = server_socket()
    host = socket.gethostname()
    port = 8999
    serv.bind((host, port))
    serv.listen(5)
    c, addr = serv.accept()
    while True:
        msg = c.recv(1024)
        server_json = json.json()
        serialized = server_json.serializer(msg)
        serialized = serialized.split()
        if serialized[0] == "signup":
            U = User(serialized[1], serialized[2], serialized[3], serialized[4])
            validation = U.validate()
            if not validation.isstring():
            #if project13_forums.model.memory.sign_up(U):
                if sign_up(U):
                    c.send(U.deserializer("Succesful"))
                else:
                    c.send(U.deserializer("Username already exists"))
            else:
                c.send(U.deserializer("Invalid Credentials " + validation))
            pass
        elif serialized[0] == "login":
            UA = UserAuth(serialized[1], serialized[2])
            validation = UA.validate()
            if not validation.isstring():
                if checkUsername(serialized[1]):
                    pw = getPassword(serialized[1])
                if pw == serialized[1]:
                    c.send(UA.deserializer('True'))
                else:
                    c.send(UA.deserializer("username password mismatch"))
            else:
                c.send(UA.deserializer("Invalid Credentials " + validation))
                pass
        elif serialized[0] == "view_forum":
            VF = ViewForum(serialized[1])
            forum_list=view_forum(VF.forum_name)
            c.send(VF.deserializer(forum_list))
            pass
        elif serialized[0] == "create_sub_forum":

            pass

    serv.close()

    pass


if __name__ == "__main__":
    server()