__author__ = 'hemavishnu'

from listutils import *

notes = """
    This is to make you familiar with linked list structures usage in python
    see the listutils.py module for some helper functions
"""


#given you a list 1->2->3->4->5 swap alternate elements and return the new head
#the new list head should result out 2->1->4->3->5

def swap_alternate_nodes_of_list(head):

    current=head
    if (current):
        next=current.next
    else:
        next=None
    if not next: return current
    head=next
    while current and current.next:
        temp=next.next

        if(temp and temp.next):
            result=temp.next
        else:
            result=temp
        current.next=result
        next.next=current
        current =temp
        if (temp):
            next=temp.next
        else:
            next=None
    return head



#write test cases covering all cases for your solution
def test_swap_alternate_nodes_of_list():
    head_node = to_linked_list([1, 2, 3, 4, 5])

    result=swap_alternate_nodes_of_list(head_node)
    assert 2 == result.value
    assert 1 == result.next.value
    assert 4 == result.next.next.value
    assert 3 == result.next.next.next.value
    assert 5 == result.next.next.next.next.value

    head_node = to_linked_list([1, 2, 3, 4, 5, 6])
    result=swap_alternate_nodes_of_list(head_node)
    assert 2 == result.value
    assert 1 == result.next.value
    assert 4 == result.next.next.value
    assert 3 == result.next.next.next.value
    assert 6 == result.next.next.next.next.value
    assert 5 == result.next.next.next.next.next.value

    head_node = to_linked_list([1])
    result=swap_alternate_nodes_of_list(head_node)
    assert 1 == result.value

    head_node = to_linked_list([1, 2])
    result=swap_alternate_nodes_of_list(head_node)
    assert 2 == result.value
    assert 1 == result.next.value