__author__ = 'SuSh'
import sys
from time import time
import os
import collections
import argparse

def load_words(path):

    words_list = []
    for f in os.listdir(path):
        file_name = os.path.join(path, f)
        with open(file_name) as f:
            sub_list = f.read().splitlines()
            words_list = words_list + sub_list
        f.close()
    return words_list

def check_anagram(word):
    word = word.strip().lower()
    word = ''.join(sorted(word))
    return word

def anagram_list(load_words):

    words = load_words
    anagrams = collections.defaultdict(list)
    for word in words:
        anagrams[check_anagram(word)].append(word)
    anagram_values = anagrams.values()
    return anagram_values

def top_anagrams(anagram_values, count, sortby):
sort by SL:
    tic = time()
    d1 = anagram_values
    d1.sort(key=lambda x :len(x), reverse=True)
    print d1[:count]
    toc = time()
    print "top_anagrams()",toc-tic

sort by AL:
d1 = anagrams.values()
    d1.sort(key=lambda x :len(x[0]), reverse=True)
    for i in range(count):
        print len(d1[i][0]),"->",d1[i]

def count(anagram_values, distribution, setsize):
    tic = time()
    d1 = anagram_values
    len_d1=len(d1)
    if setsize is None:
        setsize=2
    else:
        setsize=setsize
    d1.sort(key=lambda x :len(x), reverse=True)
    len_d1=len(d1)
    for i in range(len_d1):
        x = len(d1[i])
        if x >= setsize:
            print x, d1[i]
    if distribution is True:
        for i in range(1,12):
            s=0
            for j in range(len_d1):
                x = len(d1[j])
                if x == i:
                    s += 1
            print "Lists of size",i, s
    toc = time()
    print "count()", toc-tic


def all_word_anagrams(load_words, word):

    tic = time()
    words = load_words
    sorted_word = sorted(word)
    print [word for word in words if len(word) == len(sorted_word) and sorted(word) == sorted_word]
    toc = time()
    print "all_word_anagrams()", toc-tic


def main(argv = sys.argv):
    # add arguments checks here...
    if argv is None:
        print "No such file or directory found"
    else:
        parser= argparse.ArgumentParser()

        parser.add_argument("--root")
        parser.add_argument("--top",type=int)
        parser.add_argument("--al",action="store_true")
        parser.add_argument("--query")
        parser.add_argument("--s_size",type=int)
        parser.add_argument("--dist",action="store_true")
        args=parser.parse_args()
        words = load_words(args.root)
        assert "apple" in words
        data =top(words,args.top,args.al)
        all_word_anagrams(data,args.query)
        count(data,args.s_size,args.dist)
        assert 128985 == len(words)


if __name__ == "__main__":
    main()
