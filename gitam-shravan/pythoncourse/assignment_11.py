import sys
from time import time
import os
import collections
import argparse

#returns a merged list of all words
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

def top_anagrams(load_words, count):

    tic = time()
    words = load_words
    anagrams = collections.defaultdict(list)
    for word in words:
        anagrams[check_anagram(word)].append(word)
    d1 = anagrams.values()
    d1.sort(key=lambda x :len(x), reverse=True)
    len_d1=len(d1)
    for i in range(len_d1):
        x = len(d1[i])
        if x >= count:
            print x, d1[i]
    toc = time()
    print toc-tic

def all_word_anagrams(load_words, word):
    t = time()
    words = load_words
    sorted_word = sorted(word)
    print [word for word in words if len(word) == len(sorted_word) and sorted(word) == sorted_word]
    t1=time()
    print t1-t

def main(argv = sys.argv):
    # add arguments checks here...

    words = load_words(sys.argv[1])
    assert "apple" in words
    assert 128985 == len(words)

    parser = argparse.ArgumentParser()
    parser.add_argument('count', type= int, help="Enter the top anagram count",dest="count")
    parser.add_argument('-query', action="store", help="Enter the string", dest="query")
    args = parser.parse_args()
    if args.count:
        top_anagrams(words, args.count)
    elif args.query:
        all_word_anagrams(words, args.query)


    #top_anagrams(words, 7)
    #query = raw_input("Enter any String")
    #all_word_anagrams(words, query)


if __name__ == "__main__":
    main()
