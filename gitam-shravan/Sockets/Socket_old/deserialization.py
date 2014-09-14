
import os
import sys
import inspect

#Serialization
dict={'request_type':['view','write','create','exit'],'forum_name':['algo','datastr'],'msg':''}
dict1={}

def mylen(input1):
    length = 0
    for ch in input1:
        length += 1
    return length

def endIndexOf(whole,sub):
    i = 0
    j = 0
    length = mylen(whole)
    sublen = mylen(sub)
    while i <= length-sublen :
        if whole[i] == sub[j]:
            presence = True
            j = 1
            while j < sublen:
                if whole[i+j] != sub[j]:
                    presence = False
                    break
                j += 1
            if presence:
                return (i+j-1)
                break
            i = i+j-1
            j=0
        i += 1
    return -1

def getUptoChar(input1,start,delimiter):
    buff = str()
    try:
        while input1[start] != delimiter:
            buff += input1[start]
            start += 1
    except IndexError as ie:
        pass
    print buff,":buffer 45"
    return buff


def create(filename,message):
    f=open(filename,"wb")
    f.write(message)
    f.close()

def view(filename):
    mod_file = inspect.getfile(inspect.currentframe())
    mod_dir = os.path.dirname(mod_file)
    file=os.path.join(mod_dir, filename)
    f=open(file,"rt")
    for i in f.readlines():
        print i
    f.close()

def write(filename,msg):
    mod_file = inspect.getfile(inspect.currentframe())
    mod_dir = os.path.dirname(mod_file)
    file=os.path.join(mod_dir, filename)
    with open(file,"a") as f:
        f.write(msg)
    f.close()

def get_file_path(file):
    mod_file = inspect.getfile(inspect.currentframe())
    mod_dir = os.path.dirname(mod_file)
    return os.path.join(mod_dir, file)

class json():
    def __init__(self,request_type='',forum_name='',msg=''):
        self.request_type=request_type
        self.forum_name=forum_name
        self.msg=msg
        self.dict1=dict1
    def serialization(self,obj):
        dict1['request_type']=obj.request_type
        dict1['forum_name']=obj.forum_name
        dict1['msg']=obj.msg
        print str(dict1),":91"
        return str(dict1)

    def deserialization(self,message):
        print message
