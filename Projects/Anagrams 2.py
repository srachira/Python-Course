__author__ = 'Kalyan'

notes = '''
This assignment requires you to use all that you have learnt to write elegant and compact code to build up this project,
we will add more requirement to this project every day.

1. Download the english word list from http://dreamsteep.com/projects/the-english-open-word-list.html and unzip it
   to some directory. You will see a list of word files in your directory. for e.g C:\work\EOWL-words\LF Delimited Format

2. Take the directory above as an argument to this program when you run it from command line (as python assignment_11.py <root>)

3. Read all the *words.txt files and populate words from each into a single list. As you read each file, print out the
   number of words in each file. Finally print out the total number of words read. These should match the counts mentioned
   in the above url.

4. We will extend this module to do many things over the next few days.

'''

import argparse
import collections
import sys
import os
import time
def query(list1,word):
    t1=time.clock()
    result=[]
    for each in list1:
        if word in each:
            result.append(each)
    print result
    t2=time.clock()
    print "the time taken by query method is",(t2-t1)
    print "--------------------------------------------------------------------------------"

# for finding anagrams
def count(list,set_size,dist):
    toc=time.clock()
    if set_size is None:
          set_size=2
    else:
        set_size=set_size
    temp=[each for each in list for word in each if len(each)==set_size]
    print temp
    leng=1
    if dist is True:
            count1=collections.Counter()
            for each in list:
               count1[len(each)]+=1
            for each in count1.items():
                  print each[0],"--->",each[1]
    tic=time.clock()
    print "the time taken by count method is",tic-toc
    print "------------------------------------------------------------------------------"

def top(res_list,count,criteria):

    t1=time.clock()
    anagrams_list = collections.defaultdict(list)
    for word in res_list:
        anagrams_list[''.join(sorted(word))].append(word)
    words= anagrams_list.values()
    for each in words:
        if '\\' in each:
            words.delete(each)
    if criteria is True:
        words.sort(key=lambda x:len(x[0]),reverse=True)
        print words[0:count]
    else:
        words.sort(key=len, reverse=True)
        for i in range(count):
              print len(words[i]),"-->",words[i]
    t2=time.clock()
    print "the time taken by top_count is",(t2-t1)
    print "-----------------------------------------------------------------------------"
    return words

#returns a merged list of all words
def load_words(base_dir):
    t1=time.clock()
    word_list=[]
    os.chdir(base_dir)
    count=0
    for files in os.listdir(base_dir):
        f=open(files,"rb")
        for line in f.readlines():
                word_list.append(str(line.decode('ascii','ignore')).rstrip("\n"))
                count+=1
        count=0

    print len(word_list)
    t2=time.clock()
    print "the time taken by load_words is",(t2-t1)
    print "-----------------------------------------------------------------------------"
    return word_list




def main(argv = sys.argv):
    # add arguments checks here...
    parser= argparse.ArgumentParser()
    parser.add_argument("--root")
    parser.add_argument("--top",type=int)
    parser.add_argument("--al",action="store_true")
    parser.add_argument("--query")
    parser.add_argument("--s_size",type=int)
    parser.add_argument("--dist",action="store_true")
    args=parser.parse_args()
    words = load_words(args.root)
    data =top(words,args.top,args.al)
    query(data,args.query)
    count(data,args.s_size,args.dist)

    assert "apple" in words
    assert 128985 == len(words)



if __name__ == "__main__":
    main()
