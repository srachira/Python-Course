__author__ = 'Kalyan'

notes = '''
sets are  unordered collection of elements without duplicates. Conceptually they are similar to dicts except that
the keys are not associated with any values.
'''

from placeholders import  *

def test_set_type():
    test_set = {"one", "two", "three"}   # note the new syntax
    assert 'set' == type(test_set).__name__

def test_set_empty():
    empty_set_wrong = {""}  #curly braces are used for both sets and dicts, so how do you disambiguate?
    #by giving {""} i.e. set empty.. Note that sets are not associated with keys
    # so "" represents an empty element & as we have {};it represents a set.
    assert True == isinstance(empty_set_wrong, set)

    empty_set = set()
    assert True == isinstance(empty_set, set)
    assert 0 == len(empty_set)

def test_set_length():
    fruits = {"apple", "apple", "apple"}
    assert 1 == len(fruits)  #are duplicates removed?
    #Yes, sets do not have duplicates
    #Sets do not support indexing! :)

    veggies = {"beetroot", "potato", "spinach"}
    assert 3 == len(veggies)

def test_set_creation():
    """
    sets can be created from any sequence like list or a tuple.
    """
    test_list = [1, 2, 1, 3]
    set1 = set(test_list)
    assert set([1, 2, 3]) == set1

    test_string = "apple"
    set2 = set(test_string)
    assert set(['a', 'p', 'e', 'l']) == set2

    test_dict = { 1: "one", 2 : "two"}
    set3 = set(test_dict)
    assert set([1, 2]) == set3

    set4 = set(test_dict.values())
    assert set(['two', 'one']) == set4

    set5 = set(test_dict.items())
    assert set([(2, 'two'), (1, 'one')]) == set5

def test_set_membership():
    fruits = {"apple", "mango", "kiwi"}
    assert (True) == ("apple" in fruits)
    assert (False) == ("dog" in fruits)

def test_set_operations():
    set1 = {"one", "two", "three"}
    set2  =  {"three", "four"}

    all = set1 | set2 # union
    assert set(['four', 'three', 'two', 'one']) == all

    common = set1 & set2
    assert set(['three']) == common

    diff1 = set1 - set2
    assert set(['two', 'one']) == diff1

    diff2 = set2 - set1
    assert set(['four']) == diff2

    diff3 = set1 - set1
    assert set([]) == diff3

    diff4 = set1.symmetric_difference(set2)
    assert set(['four', 'two', 'one']) == diff4

    #read up help on other method using the help method in the python console.

def test_set_valid_members():
    test_set = set()
    test_set.add("hello")
    test_set.add(1)
    test_set.add((1,2))

    try:
        test_set.add([])
    except TypeError as te:
        print te
        #error is unhashable type: 'list'
        assert True

    try:
        test_set.add((1,[]))
    except TypeError as te:
        print te
        #error is unhashable type: 'list'
        assert True

    assert set([(1, 2), 1, 'hello']) == test_set

three_things_i_learnt = """
-Sets are unordered lists with distinct values. Sets are same as dictionaries but with no values.
-Duplicates are not allowed in sets, they are removed!
-Conversion of strings and dictionaries into sets.In Strings duplicates are removed,
same with dictionaries duplicates are removed and only keys are printed!
-Opearations on sets union,intersection,difference,remove,issubset,
symmetric_difference,clear and add!
-Sets are immutable.. :)
"""

time_taken_minutes = 25


