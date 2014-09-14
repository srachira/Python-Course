__author__ = 'Kalyan'

notes = '''
1. Read instructions for each function carefully.
2. Feel free to create new functions if needed. Give good names though :)
3. Try to use builtins and datastructures instead of writing your own.
4. If something about the function spec is not clear, use the corresponding test
   for clarification
'''

from placeholders import *

def sort_by_length(words):
    x=words
    if(words is not None):
        x.sort(key=len, reverse=True)
        return x
    elif(x is None):
        return None

def top_chars(word, n):
    x = word
    d = dict((c, x.count(c)) for c in set(x))
    d1 = d.items()
    d1.sort(key=lambda x: (-x[1], x[0]))
    return d1[:n]

def test_sort_by_length():
    assert ["apple", "bear", "dog"] == sort_by_length(["dog", "apple", "bear"])
    assert ["apple", "bear", "dog"] == sort_by_length(["apple", "dog",  "bear"])
    assert ["apple", "dog", "cat"] == sort_by_length(["dog", "apple", "cat"])
    assert ["elephant", "apple"] == sort_by_length(["apple", "elephant"])
    assert ["three", "four", "one", "two"] == sort_by_length(["one", "two", "three", "four"])
    assert [] == sort_by_length([])
    assert None == sort_by_length(None)

def test_top_chars():
    assert [('p', 2)] == top_chars("app",1)
    assert [('p', 2), ('a',1)] == top_chars("app",2)
    assert [('p', 2), ('a',1)] == top_chars("app",3)

    assert [('a', 2)] == top_chars("aabc", 1)
    assert [('a', 2), ('b', 1)] == top_chars("aabc", 2)
    assert [('a', 2), ('b', 1), ('c', 1)] == top_chars("aabc", 3)

    assert [('e', 3)] == top_chars("irreversible", 1)
    assert [('e', 3), ('r', 3)] == top_chars("irreversible", 2)
    assert [('e', 3), ('r', 3), ('i',2), ('b', 1)] == top_chars("irreversible", 4)

three_things_i_learnt = """
-Learnt about the usage of LAMBDA function.
-Sorting of lists.
-Sorting by word length instead of word content.
-Finding the frequency counts of characters and their respective counts..
-Returning the top most counts using the lambda function. :)
"""

time_taken_minutes = 90