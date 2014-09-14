_author__ = 'Dixith Kurra,chaitanya'

import threading
from backend.store import *
from backend.projectutils import *
from backend.filecreation import *

list1 = []  #category1
list2 = []  #2
list3 = []  #3
list4 = []  #4
list5 = []  #5
list6 = []  #6
list7 = []  #7

user_metadata = []
forum_metadata = []
sub_forum_metadata = [list1, list2, list3, list4, list5, list6, list7]

lock=threading.Lock()


def check_username_availability(username):
    for i in user_metadata:
        if username==i.name:
            return False
    return True


def sign_up(user_obj):
    for i in user_metadata:
        if user_obj.name!=i.name:
            pass
        else:
            return False
    return insert(user_obj)

def insert(user_obj):
    lock.acquire()
    addUserMetadata(user_obj)  #call backend
    user_metadata.append(user_obj)
    lock.release()
    return True


def sign_in(user_sign_in_obj):
    for i in user_metadata:
        if i.name==user_sign_in_obj.name and i.password==user_sign_in_obj.password:
            return True  # print 'authorized user'
    return False # print 'invalid user'


# create subforum in a particular category
def create_sub_forum(sub_forum_obj): #3 fileds in sub_form_obj
    forum_name=sub_forum_obj.forumname
    i=get_number(forum_name)
    sub_forum_name = sub_forum_obj.name
    lock.acquire()
    for k in sub_forum_metadata[i-1]:
        if k.name==sub_forum_name:
            return False
    writesubForumData(sub_forum_obj) #call backend
    sub_forum_metadata[i-1].append(sub_forum_obj)
    lock.release()
    return True
    pass

def get_number(forum_name):
    if forum_name == "Education":
        return 1
    elif forum_name == "Sports":
        return 2
    elif forum_name == "Entertainment":
        return 3
    elif forum_name == "Technology":
        return 4
    elif forum_name == "News":
        return 5
    elif forum_name == "Health":
        return 6
    elif forum_name == "Miscellaneous":
        return 7

# display forums in particular category
# for example display forums in education
def view_forum_in_memory(forum_obj):
    forum_name=forum_obj.name
    i=get_number(forum_name)
    view_sub_forum_list=[]
    for k in sub_forum_metadata[i-1]:
        temp=[]
        temp.append(k.id)
        temp.append(k.name)
        temp.append(k.createdby)
        view_sub_forum_list.append(temp)
    return view_sub_forum_list

'''def delete_sub_forum(i,sub_forum_name):
    pass
    pass
    for k in sub_forum_metadata[i]:
        if k.forum_name==sub_forum_name:
            del k
            return True
    return False
'''

#view questions in a particular sub-forum
#for eg: view questions in education/computers
def view_que_in_subforum(sub_forum_obj):
    msg_id_list,postedBy_list=viewQuestions(sub_forum_obj)
    print msg_id_list
    try:
       fp=open(file,'rb+')
       msg_list=[]
       i=0
       while i+1<len(msg_id_list):
          fp.seek(msg_id_list[i])
          msg=fp.read(msg_id_list[i+1]-msg_id_list[i])
          temp_list=[msg_id_list[i],msg,postedBy_list[i]]
          msg_list.append(temp_list)
          i+=1
    except Exception:
         pass
    finally:
         fp.close()
    return msg_list


def view_replies_for_que_in_sub_forum(que_obj):
    rply_id_list= viewReplies(que_obj)
    try:
       fp=open(file,'rb+')
       rply_list=[]
       i=0
       while i+1<len(rply_id_list):
          fp.seek(rply_id_list[i])
          reply=fp.read(rply_id_list[i+1]-rply_id_list[i])
          temp_list=[rply_id_list[i],reply]
          rply_list.append(temp_list)
          i+=1
    except Exception:
        pass
    finally:
        fp.close()
    return rply_list

    pass


def post_msg_in_sub_forum(msg_obj):
    lock.acquire()
    msg_status=writeMessageData(msg_obj)   #call backend
    lock.release()
    return msg_status
    pass


def post_rply_in_sub_forum(rply_obj):
    lock.acquire()
    rply_status=writereplyData(rply_obj)   #call backend
    lock.release()
    return rply_status
    pass


def getFilePath(filename):
    mod_file=inspect.getfile(inspect.currentframe())
    mod_dir=os.path.dirname(mod_file)
    file=os.path.dirname(mod_file)
    return file

def load_database():

    file=getFilePath(filename="file.bin")
    #def load_user_metadata():

    try:
        fp = open(file,'rb+')
        fp.seek(1526)
        user_count = struct.unpack('I', fp.read(4))[0]
        c = 1
        while c <= user_count:
            obj = User(None, None, None, None, None)
            obj.id = struct.unpack('I', fp.read(4))[0]
            obj.name = fp.read(20).strip('\x00')
            obj.password = fp.read(10).strip('\x00')
            obj.mail = fp.read(30).strip('\x00')
            obj.birth_date = fp.read(10).strip('\x00')
            obj.join_date = fp.read(10).strip('\x00')
            fp.read(104 - 84)
            user_metadata.append(obj)
            c += 1


        #def load_forum_metadata():
        fp.seek(1026)
        forum_count = struct.unpack('I', fp.read(4))[0]
        c = 1
        while c <= forum_count:
            obj = Forum(0, '')
            obj.id = struct.unpack('I', fp.read(4))[0]
            obj.name = fp.read(30).strip('\x00')
            obj.nextForum = struct.unpack('I', fp.read(4))[0]
            obj.prevForum = struct.unpack('I', fp.read(4))[0]
            obj.firstsubForum = struct.unpack('I', fp.read(4))[0]
            fp.read(70 - 46)
            forum_metadata.append(obj)
            c += 1


        #def load_sub_forum_metadata():
        fp.seek(43526)
        sub_forum_count = struct.unpack('I', fp.read(4))[0]
        c = 1
        while c <= sub_forum_count:
            obj = SubForum(None, None, None)
            obj.id = struct.unpack('I', fp.read(4))[0]
            obj.name = fp.read(30).strip('\x00')
            obj.forumname = fp.read(30).strip('\x00')
            i=get_number(obj.forumname)
            obj.createdby = fp.read(20).strip('\x00')
            obj.nextSubForum = struct.unpack('I', fp.read(4))[0]
            obj.prevSubForum = struct.unpack('I', fp.read(4))[0]
            obj.firstQuestion = struct.unpack('I', fp.read(4))[0]
            obj.num_of_questions = struct.unpack('I', fp.read(4))[0]
            fp.read(124 - 100)
            sub_forum_metadata[i-1].append(obj)
            c += 1
    except Exception:
        pass
    finally:
        fp.close()

