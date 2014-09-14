__author__ = 'Kalyan'

notes = '''
Fill up each of this methods so that it does what it is intended to do. Use
only the standard data types we have seen so far and builtin functions.

builtin functions: http://docs.python.org/2/library/functions.html

Do not use any control flow statements (if, for...) in this assignment.
Assume that inputs are valid and of expected type, so no checking required.

use constants from string module (string.XXXX) as required.
'''

from placeholders import *

import string



def get_lower_to_upper_dict():

    x=tuple(string.lowercase)
    x=sorted(x)
    y=tuple(string.uppercase)
    y=sorted(y)
    return dict(zip(x,y))

def get_digit_to_string_dict():
    x=range(0,10)
    y=tuple(string.digits)
    y=sorted(y)
    return dict(zip(x,y))

three_things_i_learnt = """
-Mapping using the zip function.
-Dictionary which maps Digit to its String representation using zip
-String modules and using them by using import.string
"""

time_taken_minutes = 40

def test_lower_to_upper_dict():
    lower_to_upper = get_lower_to_upper_dict()
    assert 26 == len(lower_to_upper)
    for x in lower_to_upper:
        y = lower_to_upper[x]
        assert 1 == len(x)
        assert x.islower()
        assert 1 == len(y)
        assert y.isupper()
        assert x.upper() == y


def test_digit_to_string_dict():
    digit_to_string = get_digit_to_string_dict()
    assert 10 == len(digit_to_string)
    for x in range(0,10):
        assert x in digit_to_string
        assert digit_to_string[x] == str(x)
