__author__ = 'Kalyan'

notes = '''
This assignment requires you to use all that you have learnt to write elegant and compact code to build up this project,
we will add more requirement to this project every day.

1. Download the english word list from http://dreamsteep.com/projects/the-english-open-word-list.html and unzip it
   to some directory. You will see a list of word files in your directory. for e.g C:\work\EOWL-words\LF Delimited Format

2. Take the directory above as an argument to this program when you run it from command line (as python project_01.py <root>)

3. Read all the *words.txt files and populate words from each into a single list. As you read each file, print out the
   number of words in each file. Finally print out the total number of words read. These should match the counts mentioned
   in the above url.

4. We will extend this module to do interesting things. '''



import sys
import glob
import os
import time

#returns a merged list of all words
def load_words(base_dir):
    files = glob.glob1(base_dir, "*words.txt")
    total_words = []
    for i in files :
        fp = os.path.join(base_dir,i)
        wf = [ w.strip () for w in open(fp)]
       # print "Found"
        total_words.extend(wf)
        #print "total words is {0}".format(len(total_words))
    return total_words




def anagrams(total_words):
    initial = time.clock()
    d={}
    for  i in total_words:
        k="".join(sorted(list(i)))
        try:
            a =  d[k]
        except KeyError as se:
            d[k]=[]
            d[k].append(i)
        else:
            d[k].append(i)

    values = d.values()
    values.sort(key =len, reverse= True)
    print "time taken" ,time.clock()-initial

    return values

def anagrams_method2(total_words):
    initial = time.clock()
    list_of_tuples= []
    for i in total_words:
        j = ''.join(sorted(i))
        tuple1 = (i,j)
        list_of_tuples.append(tuple1)
    list_of_tuples.sort(key = lambda x: x[1])
    #print list_of_tuples
    anagarms_list = []

    i = 1
    try:
        while i < len(list_of_tuples)-1 :
            if list_of_tuples[i-1][1] == list_of_tuples[i][1]:
                inter = []
                while list_of_tuples[i-1][1] == list_of_tuples[i][1]:
                    inter.append(list_of_tuples[i-1][0])
                    i = i + 1
                anagarms_list.append(inter)
            i += 1

    except MemoryError:
        print "memory error"
        pass
    print "time taken" , time.clock()-initial


    return sorted(anagarms_list,key = len,reverse = True)
def are_anagrams(word1,word2):
    if len(word1)!= len(word2):
        return False
    word1 = word1.lower()
    word2 = word2.lower()
    word1 = sorted(word1)
    word2 = sorted(word2)
    if word1 == word2 :
        return True
    return False



def anagrams1(a):
    initial = time.clock()
    i,j=0,0
    inter = []
    main = []
    var1 = []
    var2 = []
    while i<len(a):
        var1 = ''.join(sorted(a[i]))
        inter = []
        j = 0
        while j<len(a):
            var2 = ''.join(sorted(a[j]))
            if i != j and var1 == var2:
                if a[i] in inter:
                    inter.append(a[j])
                else:
                    inter.append(a[i])
                    inter.append(a[j])
                a.pop(j)
                j -=1
            j += 1
        if inter!= []:
            main.append(inter)
        i +=1
    print "time taken is " , str(time.clock() - initial)
        #print main
    return sorted(main,key = len,reverse= True)


def main(argv = sys.argv):
    if len(sys.argv) <= 1:
        print "Enter in this format python project_01.py <directory_path>"
        exit(0)

    words = load_words(sys.argv[1])
    assert "apple" in words
    assert 128985 == len(words)
    result1 = anagrams(words)
    for i in range(0,4):
        print result1[i]

    result = anagrams_method2(words)
    for i in range(0,4):
        print result[i]
    result = anagrams1(words)

    for i in range(0,4):
        print result[i]


if __name__ == "__main__":
    main()













