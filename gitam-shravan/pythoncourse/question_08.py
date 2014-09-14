__author__ = 'hemavishnu'

from listutils import*
from question_06 import *
notes = """
    This is to make you familiar with linked list structures usage in python
    see the listutils.py module for some helper functions
"""


#Given sorted list with one sublist reversed,
#find the reversed sublist and correct it
#Ex: 1->2->5->4->6->7
# sort the list as: 1->2->4->5->6->7
def sort_reversed_sublist(head):
    current=head
    temp=None
    while ((current.next is not None) and current.value <= current.next.value ):
        temp=current
        current=current.next
    start=current
    while ((current.next is not None) and current.value >= current.next.value ):
        current=current.next
    last=current.next
    current.next=None
    first=reverse_linked_list(start)

    if temp is not None:
        temp.next=first
    else:
        temp=head

    while first.next is not None:
        first=first.next
    first.next=last

    while head:
        print head.value
        head=head.next
    return head

#write test cases covering all cases for your solution
def test_sort_reversed_sublist():
    head_node = to_linked_list([1, 2, 3, 1,2,3,4,5])
    result=sort_reversed_sublist(head_node)
    while result is not None:
        print result.value
        result=result.next

    head_node = to_linked_list([1,2,10,9,8,7,6,5,4,3,11])
    result=sort_reversed_sublist(head_node)
    head_node = to_linked_list([1,10,9,8,7,6,5])
    result=sort_reversed_sublist(head_node)
    head_node = to_linked_list([1,2,3,6,5,4])
    result=sort_reversed_sublist(head_node)
    head_node = to_linked_list([3,2,1,4,5,6,7,8])
    result=sort_reversed_sublist(head_node)

