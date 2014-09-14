
import os
import time
import argparse
import sys

def replaceit(st, put, pos):
    st=list(st)
    count = 0
    st[pos]= put
    st="".join(st)
    return st

def load_words(base_dir,length):
    t1=time.clock()
    word_list=[]
    os.chdir(base_dir)
    count=0
    for files in os.listdir(base_dir):
        f=open(files,"rb")
        for line in f.readlines():
            if len(line.rstrip("\n")) == length:
                word_list.append(str(line.decode('ascii','ignore')).rstrip("\n"))
                count+=1
        print " Found {0} words in {1}".format(count,f.name)
        count=0
    print len(word_list)
    t2=time.clock()
    print "the time taken by load_words is",(t2-t1)
    print "-----------------------------------------------------------------------------"
    return word_list


def chain(words,start,end):
    count=0
    if len(start) != len(end):
        return "Start length and end length not same!"
    path=[]
    path.append(start)
    length=len(start)
    temp=start
    flag=0
    while temp is not end and flag == 0:
        if temp == end:
            flag=1
            break
        for j in range(length-1,-1,-1):
            if temp[j] != end[j]:
                a= temp[j]
                temp=replaceit(temp,end[j],j)
                if temp in words:
                    path.append(temp)
                    count=0
                    break
                elif count == length-1 and temp not in words:
                    temp=replaceit(temp,chr(ord(a)+1),j)
                    count = 0
                    while temp not in words:
                        temp =replaceit(temp,chr(ord(temp[j])+1),j)
                    path.append(temp)
                    #j=length-1
                    break
                else:
                    count+=1
                    temp=replaceit(temp,a,j)
    print path

def main(argv = sys.argv):
    # add arguments checks here...
    if argv is None:
        print "No such file or directory found"
    else:
        parser= argparse.ArgumentParser()
        parser.add_argument("--root")
        args=parser.parse_args()
        start="black"
        destination="white"
        length_given=len(start)
        words=load_words(args.root,length_given)
        t1=time.clock()
        chain(words,start,destination)
        t2=time.clock()
        print "the time taken by chain is",(t2-t1)
if __name__ == "__main__":
    main()
