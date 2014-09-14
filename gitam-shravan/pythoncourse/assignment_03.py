__author__ = 'Kalyan'

notes = '''
1. Read instructions for each function carefully.
2. Try to use builtins and data structures instead of writing your own.
3. If something about the function spec is not clear, use the corresponding test
   for clarification
'''
from placeholders import *
import string

# Convert a sentence which has either or to only the first choice.
# e.g we could either go to a movie or a hotel -> we could go to a movie.
# note: do not use intermediate lists, only use string functions
# assume words are separated by spaces. you can use control flow statements

def prune_either_or(sentence):
    ch = sentence
    ch=ch.split()
    if("either" in ch):
        if("or" in ch):
            ch.remove("either")
            x=ch.index("or")
            ch1=ch[:x]
            ch1=" ".join(ch1)
            return ch1
        else:
            ch2=" ".join(ch)
            return ch2

# Create a palindrome of twice the length of the word passed in.
# e.g. app -> appppa, bat -> battab etc.
# hint: look up extended slice notation.

def create_palindrome(word):
    x=word
    if(x is not None):
        y=x[::-1]
        z="".join([x,y])
        return z
    elif(x is None):
        return None


# returns a dict which maps a -> 1, b -> 2 ... z->26 and A -> 1, B ->2 ... Z->26
# no control flow allowed.
def get_encoding_dict():

    x=dict(zip(string.uppercase, range(1, len(string.uppercase) + 1)))
    y=dict(zip(string.lowercase, range(1, len(string.lowercase) + 1)))
    z = dict(x.items() + y.items())
    return z


def test_either_or_pruning():
    assert "We can go to a movie" == prune_either_or("We can either go to a movie or a hotel")
    assert "We can go either way" == prune_either_or("We can go either way")
    assert "" == prune_either_or("either or")
    assert "either way is fine" == prune_either_or("either way is fine")

def test_create_palindrome():
    assert "battab" == create_palindrome("bat")
    assert "abba" == create_palindrome("ab")
    assert "" ==create_palindrome("")
    assert None == create_palindrome(None)

def test_get_encoding_dict():
    d = get_encoding_dict()
    assert len(d) == 52
    for key in d:
        assert ord(key.lower()) - ord('a') + 1 == d[key]

three_things_i_learnt = """
-Converting a statement into a single first choice
-Creating a palindrome by using the extended slice concept
-Mapping numbers to both uppercase and lowercase alphabets and using zip to convert them into a dict.
-Adding items of two dictionaries by using the union operator
"""

time_taken_minutes = 50