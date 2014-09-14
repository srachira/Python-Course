__author__ = 'amani,surya',
import os
import inspect
import datetime
import struct
from projectutils import *


def getFilePath(filename):
    mod_file=inspect.getfile(inspect.currentframe())
    mod_dir=os.path.dirname(mod_file)
    file=os.path.join(mod_dir,filename)
    return file

def forumcreation():
    forum_count=0
    offset=70
    forum_list=["Education","Sports","Entertainment","Technology","News","Health","Miscellaneous"]
    forum_object_list=[]
    for forum_name in forum_list:
        id=1030+offset*forum_count
        forum_object=Forum(id=id,name=forum_name)
        forum_object_list.append(forum_object)
        forum_count+=1
    num_of_forums=len(forum_object_list)
    #print num_of_forums
    i=0
    while i<num_of_forums-1:
        forum_object_list[i].nextForum=forum_object_list[i+1].id
        i+=1
    while i>0:
        forum_object_list[i].prevForum=forum_object_list[i-1].id
        i-=1
    for forum_object in forum_object_list:
        writeForumData("file.bin",forum_object)
    #print "successfully forums created"

def writeForumData(filename,forumdata):
    file=getFilePath(filename)
    with open(file,"rb+") as f:
        f.seek(1026)
        forum_count=struct.unpack('I',f.read(4))[0]
        f.seek(1030+70*forum_count)
        f.write(struct.pack('i',forumdata.id))
        f.write(struct.pack('30s',forumdata.name))
        f.write(struct.pack('i',forumdata.nextForum))
        f.write(struct.pack('i',forumdata.prevForum))
        f.write(struct.pack('i',forumdata.firstsubForum))
        f.write(struct.pack('i',forumdata.num_of_subforums))
        f.write(struct.pack('i',forumdata.num_of_views))
        forum_count+=1
        f.seek(1026)
        f.write(struct.pack('I',forum_count))
    f.close()

def writeUserData(filename,userdata):
    file=getFilePath(filename)
    with open(file,"rb+") as f:
        f.seek(1526)
        user_count=struct.unpack('I',f.read(4))[0]
        user_id=1530+128*user_count
        f.seek(user_id)
        f.write(struct.pack('i',user_id))
        f.write(struct.pack('20s',userdata.name))
        f.write(struct.pack('10s',userdata.password))
        f.write(struct.pack('30s',userdata.mail))
        t=datetime.date(userdata.birth_date[0],userdata.birth_date[1],userdata.birth_date[2])
        strTime=t.strftime('%y-%m-%d')
        f.write(struct.pack('10s',strTime))
        joinTime=userdata.join_date.strftime('%y-%m-%d')
        f.write(struct.pack('10s',joinTime))
        f.write(struct.pack('i',userdata.num_of_posted_messages))
        user_count+=1
        f.seek(1526)
        f.write(struct.pack('I',user_count))
    f.close()
    return True

def writeSubforumdata(filename,subforumData):
    file=getFilePath(filename)
    with open(file,"rb+") as f:
        f.seek(43526)
        subforum_count=struct.unpack('I',f.read(4))[0] #update global count of num of sub forums
        subforum_id=43530+124*subforum_count
        subforumData.id=subforum_id
        # subforum_count+=1
        # f.seek(43526)
        # f.write(struct.pack('I',subforum_count))
        forumaddr=getForumId(filename,subforumData.forumname)
        f.seek(forumaddr+46)
        count=struct.unpack('I',f.read(4))[0]                    #update forum subforum-count
        count+=1
        f.seek(forumaddr+46)
        f.write(struct.pack('I',count))
        f.seek(forumaddr+42)
        firstsubF=struct.unpack('i',f.read(4))[0]
        if firstsubF==-1:                                       #update first subforum addr
            f.seek(forumaddr+42)
            f.write(struct.pack('I',subforumData.id))
            subforumData.prevSubForum=forumaddr
            # insertSubFmetadata(filename,subforumData)
        else:
            temp=0
            while firstsubF!=-1:
                temp=firstsubF
                f.seek(firstsubF+88)
                print "read",f.read(4)                                #update prev and next subforum pointers
                nextsubFaddr=struct.unpack('i',f.read(4))[0]
                firstsubF=nextsubFaddr
            f.seek(temp+88)
            f.write(struct.pack('i',subforumData.id))
            subforumData.prevSubForum=temp
        insertSubFmetadata(filename,subforumData)


def insertSubFmetadata(filename,subforumData):
    file=getFilePath(filename)
    with open(file,"rb+") as f:
        f.seek(43526)
        subforum_count=struct.unpack('I',f.read(4))[0] #update global count of num of sub forums
        subforum_id=43530+124*subforum_count
        # subforumData.id=subforum_id
        f.seek(subforum_id)
        f.write(struct.pack('i',subforumData.id))
        f.write(struct.pack('30s',subforumData.name))
        f.write(struct.pack('30s',subforumData.forumname))
        f.write(struct.pack('20s',subforumData.createdby))
        f.write(struct.pack('i',subforumData.prevSubForum))
        f.write(struct.pack('i',subforumData.nextSubForum))
        f.write(struct.pack('i',subforumData.firstQuestion))
        f.write(struct.pack('i',subforumData.num_of_questions))
        f.write(struct.pack('i',subforumData.num_of_views))
        f.write(struct.pack('10s',subforumData.date_of_creation))
        f.write(struct.pack('10s',subforumData.last_accessed_time))
        subforum_count+=1
        f.seek(43526)
        f.write(struct.pack('I',subforum_count))
    f.close()

def insertMsgData(filename,msgdata):
    file=getFilePath(filename)
    with open(file,"rb+") as f:
        f.seek(86226)
        message_count=struct.unpack('I',f.read(4))[0]
        message_id=86230+120*message_count
        f.seek(message_id)
        msgdata.id=message_id
        f.write(struct.pack('i',msgdata.id))
        f.write(struct.pack('30s',msgdata.forumName))
        f.write(struct.pack('30s',msgdata.subForumname))
        f.write(struct.pack('20s',msgdata.postedby))
        f.write(struct.pack('I',msgdata.length))
        f.write(struct.pack('i',msgdata.nextQuestion))
        f.write(struct.pack('i',msgdata.prevQuestion))
        f.write(struct.pack('i',msgdata.firstReply))
        msg_id=actualMsgStore(msgdata)                      #store actual message
        f.write(struct.pack('i',msg_id))                    #stores location of the message
        f.write(struct.pack('i',msgdata.num_of_replies))
        f.write(struct.pack('i',msgdata.num_of_views))
        f.write(struct.pack('i',msgdata.num_of_likes))
        f.write(struct.pack('?',msgdata.isResolved))
        message_count+=1
        f.seek(86226)
        f.write(struct.pack('I',message_count))
    f.close()
    return True


def viewSubForums():
    #done in memory
    pass

def writeMessagedata(filename,messageData):
    file=getFilePath(filename)
    with open(file,"rb+") as f:
        f.seek(86226)
        message_count=struct.unpack('I',f.read(4))[0]
        message_id=86230+120*message_count
        messageData.id=message_id
        forumaddr=getForumId(filename,messageData.forumName)
        f.seek(forumaddr+42)
        firstSubId=struct.unpack('i',f.read(4))[0]
        firstMsgId=getReqSubId(filename,firstSubId,messageData)
        if firstMsgId!=-1:
            while firstMsgId!=-1:
                temp=firstMsgId
                f.seek(firstMsgId+88)
                nextMsgId=struct.unpack('i',f.read(4))[0]
                firstMsgId=nextMsgId
            f.seek(temp+88)
            f.write(struct.pack('i',messageData.id))
            messageData.prevQuestion=temp
        msg_id=actualMsgStore(messageData)
        messageData.messagedata=msg_id
        insertMsgData(filename,messageData)



def actualMsgStore(messageObj):
    file=getFilePath("data.bin")
    f=open(file,"rb+")
    f.seek(4000000)
    address=struct.unpack('I',f.read(4))[0]
    f.seek(address)
    f.write(messageObj.msg)
    position=f.tell()
    f.seek(4000000)                         #adress of free memory unit in message block
    f.write(struct.pack('I',position))
    updateUserDetails(messageObj)
    return address

def updateUserDetails(messageObj):
    uname=messageObj.postedby
    file=getFilePath("data.bin")
    f=open(file,"rb+")
    f.seek(1526)
    usercount=struct.unpack('i',f.read(4))[0]
    i=0
    while i<usercount:
        f.seek(1534+i*104)
        temp=f.read(20).strip('\x00')
        if temp==uname:
            f.seek(60,1)
            count=struct.unpack('I',f.read(4))[0]
            count+=1
            f.seek(-4,1)
            f.write(struct.pack('i',count))
            break
        i+=1
    else:
        print "no such user exists"


def getReqSubId(filename,firstSubId,messageData):
    file=getFilePath(filename)
    with open(file,"rb+") as f:
        while firstSubId!=-1:
            f.seek(firstSubId+4)
            subFname=f.read(30).strip('\x00')
            if subFname==messageData.subForumname:
                f.seek(firstSubId+96)
                count=struct.unpack('I',f.read(4))[0]
                count+=1
                f.seek(firstSubId+96)                       #inc num of questions in subforum
                f.write(struct.pack('I',count))
                f.seek(firstSubId+92)
                firstMsgId=struct.unpack('i',f.read(4))[0]
                if firstMsgId==-1:
                    f.seek(firstSubId+92)
                    f.write(struct.pack('i',messageData.id))
                    messageData.prevQuestion=firstSubId
                return firstMsgId      #returns firstquestion address
            else:
                f.seek(firstSubId+88)
                firstSubId=struct.unpack('i',f.read(4))[0]
        else:
            print "no such subforum exists"

def getFirstSubforumId(forumname):
    file=getFilePath("file.bin")
    f=open(file,"rb+")
    f.seek(1026)
    count=struct.unpack('I',f.read(4))[0]
    i=0
    while i<count:
        f.seek(1034+70*i)
        name=f.read(30).strip('\x00')
        if name==forumname:
            break
        i+=1
    else:
        print "no such forum"
        return -1
    f.seek(1072+70*i)
    id=struct.unpack('I',f.read(4))[0]
    num=struct.unpack('I',f.read(4))[0]
    return id,num

def getFirstMessageId(link1,count,subForumname):
    print "link1",link1,"count",count,subForumname
    file=getFilePath("file.bin")
    f=open(file,"rb+")
    i=0
    while i<count:
        f.seek(link1+124*i+4)
        temp=f.read(30).strip('\x00')
        print temp
        if temp==subForumname:
            print "found"
            break
        i+=1
    else:
        print "no such subforum"
    f.seek(58,1)  #seeks to the place where first message id is stored
    id=struct.unpack('I',f.read(4))[0]
    count=struct.unpack('I',f.read(4))[0]
    print id,count
    return id,count


def getQuestionIds(link2,num_of_msgs):
    idList=[]
    postedBy_list=[]
    lenList=[]
    if num_of_msgs==0:
        print "no questions in selected forum"
        return idList,postedBy_list
    else:
        file=getFilePath("file.bin")
        f=open(file,"rb+")
        i=0
        while i<num_of_msgs:
            postField=link2+64
            f.seek(postField)
            postedBy_list.append(f.read(20).strip('\x00'))
            f.seek(link2+84)
            lenList.append(struct.unpack('I',f.read(4))[0])
            link=link2+88
            f.seek(link+12)
            idList.append(struct.unpack('I',f.read(4))[0])
            f.seek(link)
            link2=struct.unpack('I',f.read(4))[0]
            i+=1
    return idList,postedBy_list,lenList



def getForumId(filename,forumname):
    file=getFilePath(filename)
    with open(file,"rb+") as f:
        f.seek(1026)
        count=struct.unpack('i',f.read(4))[0] #reads num of forums
        i=0
        while i<count:
            f.seek(1034+70*i)
            temp=f.read(30).strip('\x00')
            if temp==forumname:
                print "forum found at",i
                id= 1030+70*i
                return id
            i+=1
        else:
            print "no such forum"

def createfile(filename):
    file=getFilePath(filename)
    f=open(file,"wb")
    f.truncate(1024*1024*1024)
    f.seek(1526)
    f.write(struct.pack('I',0)) #user count
    f.seek(1026)
    f.write(struct.pack('I',0))     #forum count
    f.seek(43526)
    f.write(struct.pack('I',0))     #sub forum count
    f.seek(86226)
    f.write(struct.pack('I',0))        #message count
    f.seek(2500000)
    f.write(struct.pack('I',0))         #reply count
    f.seek(4000000)
    f.write(struct.pack('I',4194304))   #address of free message unit
    f.seek(104857620)
    f.write(struct.pack('I',104857630))     #address of free reply unit
    forumcreation()
    f.close()

if __name__=="__main__":
    #createfile("file.bin")
      # u1=User("amani","amani12","gogulaamani@gmail.com",[1992,8,4],datetime.date(2013,6,21))
      # writeUserData("file.bin",u1)
      # u2=User("ghjk","amani12","gogulaamani@gmail.com",[1992,8,4],datetime.date(2013,6,21))
      # writeUserData("file.bin",u2)
      # s1=SubForum("testing","amani","Education")
      # writeSubforumdata("file.bin",s1)
      # s2=SubForum("testing123345","amani","Education")
      # writeSubforumdata("file.bin",s2)
      # s3=SubForum("newsTesting","amani","News")
      # writeSubforumdata("file.bin",s3)
      # s4=SubForum("news2222222222222testing","amani","News")
      # writeSubforumdata("file.bin",s4)
      # s5=SubForum("sportstesting","amani","Sports")
      # writeSubforumdata("file.bin",s5)
    q1=Message("Education","testing","amani",29,id=-1,msg="how are you posting questions")
    writeMessagedata("file.bin",q1)