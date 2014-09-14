__author__ = 'amani'

import data_store
import os
import sys
import inspect


def my_len(input):
    len = 0
    for ch in input:
        len += 1
    return len


def endIndexOf(whole,sub):
    i = 0
    j = 0
    len = my_len(whole)
    sublen = my_len(sub)
    while i <= len-sublen :
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
            i = i+j-1
            j=0
        i += 1
    return -1

def getUptoChar(input,start,delimiter):
    buff = str()
    try:
        while input[start] != delimiter:
            buff += input[start]
            start += 1
    except IndexError as ie:
        pass
    return buff


def get_file_path(file):
    mod_file = inspect.getfile(inspect.currentframe())
    mod_dir = os.path.dirname(mod_file)
    return os.path.join(mod_dir, file)

def create_file(filename,message):
    f=open(filename,"wb")
    f.write(message)
    f.close()

def open_file(filename):
    mod_file = inspect.getfile(inspect.currentframe())
    mod_dir = os.path.dirname(mod_file)
    file=os.path.join(mod_dir, filename)
    f=open(file,"rt")
    for i in f.readlines():
        print i
    f.close()

def write_file(filename,msg):
    mod_file = inspect.getfile(inspect.currentframe())
    mod_dir = os.path.dirname(mod_file)
    file=os.path.join(mod_dir, filename)
    with open(file,"a") as f:
        f.write(msg)
    f.close()

class json:
    def __init__(self,req_type="",forum_name="",message=""):
        self.req_type=req_type
        self.forum_name=forum_name
        self.message=message
        self.deser=""

    def deserializer(self,input):
        print "in deserializer"
        l=input.split()
        self.req_type=l[0]
        self.forum_name=l[1]
        try:
            self.message="".join(l[2:])
        except IndexError as ie:
            pass
        return self

    def representation(self):
        if self.message is not None:
            msg="{req_type:" + self.req_type+",forum_name:"+self.forum_name+",message:"+self.message+"}"
        else:
            msg="{req_type:" + self.req_type+",forum_name:"+self.forum_name+",message:"+"None}"
        return msg

    def serializer(self,message):
        print "serializer",message
        index1=endIndexOf(message,"req_type:")
        print "index1",index1
        buff1=getUptoChar(message,index1+1,",")
        print buff1
        index2=endIndexOf(message,"forum_name:")
        buff2=getUptoChar(message,index2+1,",")
        index3=endIndexOf(message,"message:")
        buff3=getUptoChar(message,index3+1,"}")
        if buff1=="create":
            print "in create"
            data_store.data[buff2]=buff3
            filename="{0}_forum.txt".format(buff2)
            filepath = get_file_path(filename)
            create_file(filepath,buff3)
            self.deser="created successfuly"
        if buff1=="view":
            filename="{0}_forum.txt".format(buff2)
            open_file(filename)
            self.deser="forum messages submitted"
        if buff1=="post":
            filename="{0}_forum.txt".format(buff2)
            write_file(filename,buff3)
            self.deser="posted successfully"
        if buff1=="viewall":
            self.deser="\n".join(data_store.data)
        return self.deser
