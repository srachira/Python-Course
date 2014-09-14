__author__ = 'ProfAVR'

import socket
import sys
import datetime
from cache.cachefile import *

sys.path.append('E:\project13_branch\project13_forums\\api\classes')
from api.classes.user import User1
from backend.projectutils import *
from classes.UserAuth import UserAuth
from classes.ViewForum import *
from classes.ViewSubForum import *
from classes.CreateSubForum import *
from classes.postcomment import *
from classes.postQuestion import *
from classes.viewQuestion import *
from classes.JSON_Socket import *



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

    def close(self):
        self.sock.close()


def server():
    serialized={}
    serv = server_socket()
    host = socket.gethostname()
    port = 8100
    serv.bind((host, port))
    serv.listen(5)


    while True:
        c, addr = serv.accept()
        while True:
            try:
                msg = c.recv(10024)
                serialized = convert_from_json_object(msg)
                serialized_list = [None]*6
                serialized_list[0]=serialized['action']
                print serialized_list[0]
                print serialized_list
                if serialized_list[0] == "exit":
                    c.close()
                    break
                if serialized_list[0] == "signup":
                    serialized_list[1]=serialized['name']
                    serialized_list[2]=serialized['password']
                    serialized_list[3]=serialized['DOB']
                    serialized_list[4]=serialized['email']
                    serialized_list[5]=datetime.date.today()
                    U = User1(serialized_list[1], serialized_list[2], serialized_list[3], serialized_list[4],serialized_list[5])
                    validation = U.validate()
                    if not isinstance(validation,str):
                        if sign_up(U):
                            c.send(U.deserializer("Successful"))
                        else:
                            c.send(U.deserializer("Username already exists"))
                    else:
                        c.send(U.deserializer("Invalid Credentials" + validation))
                    pass
                elif serialized_list[0] == "login":
                    serialized_list[1]=serialized['name']
                    serialized_list[2]=serialized['password']
                    UA = UserAuth(serialized_list[1], serialized_list[2])
                    if sign_in(UA):
                        c.send(UA.deserializer("login successful"))
                    else:
                        c.send(UA.deserializer("username password mismatch"))
                elif serialized_list[0] == "view_forum":
                    serialized_list[1]=serialized['forumname']
                    VF = Forum(name=serialized_list[1])
                    forum_list=view_forum_in_memory(VF)
                    forum_json=convert_list(forum_list)
                    c.send(forum_json)
                    pass
                elif serialized_list[0] == "open_sub_forum":
                    serialized_list[1]=serialized['forumname']
                    serialized_list[2]=serialized['name']
                    serialized_list[3]=serialized['id']
                    VSF = SubForum(name=serialized_list[2],forumname=serialized_list[1])
                    sub_forum_question_list=view_que_in_subforum(VSF)
                    question_json=convert_list(sub_forum_question_list)
                    print question_json,"104"
                    c.send(str(question_json))

                elif serialized_list[0] == "new_sub_forum":
                    serialized_list[1]=serialized['forumname']
                    serialized_list[2]=serialized['name']
                    serialized_list[3]=serialized['createdby']
                    CSF = SubForum(serialized_list[2],serialized_list[3],serialized_list[1])
                    if create_sub_forum(CSF):
                        c.send(CSF.deserializer(serialized_list[2]+" subforum is created"))
                    else:
                        c.send(CSF.deserializer("subforum name already exists"))


                elif serialized_list[0] == "post_question":
                    serialized_list[1]=serialized['forumname']
                    serialized_list[2]=serialized['sub_forum']
                    serialized_list[3]=serialized['createdby']
                    serialized_list[4]=serialized['new_question']
                    serialized_list[5]=len(serialized['new_question'])
                    PQ = Message(forumname=serialized_list[1],subForumname=serialized_list[2],postedby=serialized_list[3],length=serialized_list[5],msg=serialized_list[4])
                    if post_msg_in_sub_forum(PQ):
                        c.send(PQ.deserializer("successfully posted"))
                    else:
                        c.send(PQ.deserializer("unsuccessful"))
                elif serialized_list[0] == "post_answer":
                    serialized_list[1]=serialized['sub_forum']
                    serialized_list[2]=serialized['createdby']
                    serialized_list[3]=serialized['new_reply']
                    serialized_list[4]=serialized['forumname']
                    serialized_list[5]=serialized['question_id']
                    print serialized_list[5]
                    print type(serialized_list[5])
                    PC=Reply(forumname=serialized_list[4],subForumname=serialized_list[1],message_id=int(serialized_list[5]),postedby=serialized_list[2],msgLength=len(serialized_list[3]),msg=serialized_list[3])
                    if post_rply_in_sub_forum(PC):
                        c.send(PC.deserializer("successfully posted"))
                    else:
                        c.send(PC.deserializer("unsuccesfull in posting a reply"))
                elif serialized_list[0] == "view_question":
                    serialized_list[1]=serialized['forumname']
                    serialized_list[2]=serialized['sub_forum']
                    serialized_list[3]=serialized['question_id']
                    VQ=Message(forumname=serialized_list[1],subForumname=serialized_list[2],id=serialized_list[3])
                    reply_list=view_replies_for_que_in_sub_forum(VQ)
                    c.send(VQ.deserializer(reply_list))
                    pass
            except Exception as e:
                print e," Error"
    serv.close()

if __name__ == "__main__":
    load_database()
    server()
