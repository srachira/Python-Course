__author__ = 'hemavishnu'

from listutils import *
#
notes = """
    This is to make you familiar with linked list structures usage in python
    see the listutils.py module for some helper functions
"""


#given the head of a list,
# reverse the list and return the head of the reversed list
def reverse_linked_list(head):
     if (not(head and head.next)):
        return head
     result = reverse_linked_list(head.next)
     head.next.next = head
     head.next = None
     return result

#write test cases covering all cases for your solution
def test_reverse_linked_list():
    head1=to_linked_list([1,2,3,4,5])
    result=reverse_linked_list(head1)
    head1=to_linked_list([1,2,3])
    result=reverse_linked_list(head1)
    assert 3 == result.value
    assert 1 == result.next.next.value
    head1=to_linked_list([1])
    result=reverse_linked_list(head1)
    assert 1 == result.value
