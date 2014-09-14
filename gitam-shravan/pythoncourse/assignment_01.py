__author__ = 'Kalyan'

from placeholders import *

notes = '''
Fill up each of this methods so that it does what it is intended to do. Use
only the standard data types we have seen so far and builtin functions.

builtin functions: http://docs.python.org/2/library/functions.html

Do not use any control flow statements (if, for...) in this assignment.
Assume that inputs are valid and of expected type, so no checking required.
'''


def get_odds_list(count):

    x=count*2
    y=range(1,x,2)
    y.reverse()
    return y

def get_sorted_diff_string(first, second):

    y = set(first) - set(second)
    y=sorted(y)
    return "".join(y)

def get_sorted_without_duplicates(input):

    x=set(input)
    x=sorted(x)
    return "".join(x)


three_things_i_learnt = """
-Proper usage of the range function
-Set can be used to eliminate duplicates and even find difference
-Set used along with sorted function can return the answer in a sorted manner
-"Sorted" a built-in function can sort sets :)
"""

time_taken_minutes = 30


def test_odds_list():
    assert [1] == get_odds_list(1)
    assert [] == get_odds_list(0)
    assert [5,3,1] == get_odds_list(3)
    assert [9,7,5,3,1] == get_odds_list(5)

def test_sorted_diff_string():
    assert "" == get_sorted_diff_string("apple", "apple")
    assert "aelp" == get_sorted_diff_string("apple", "")
    assert "do" == get_sorted_diff_string("dog", "pig")
    assert "in" == get_sorted_diff_string("pineapple", "apple")


def test_sorted_without_duplicates():
    assert "aelp" == get_sorted_without_duplicates("apple")
    assert "eorz" == get_sorted_without_duplicates("zeroo")
    assert "" == get_sorted_without_duplicates("")
    assert "abcd" == get_sorted_without_duplicates("abcdabcd")

