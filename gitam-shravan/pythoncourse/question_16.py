__author__ = 'Kalyan'

notes = '''
This problem deals with circular single linked lists, the tail of the list points back to head.

For this assignment assume that input list is sorted (ie) smallest element is head.
'''

from listutils import *

#insert a new node into the circular linked list so that the circular list loop sorted invariant holds




def insert_node(head, value):
    current=head
    if head==None:
        head=Node
        head.value=value
        head.next=head
        last=head
        return head

    elif current.value>=value:
        while current.next!=head:
            current=current.next
        p=Node
        current.next=p
        p.value=value
        p.next=head
        head=p
    else:
        while current.next!=head and current.next.value<value:
            current=current.next
        p=Node
        p.value=value
        p.next=current.next
        current.next=p
    return head


def check_insertion(input, value, output):
    head = to_circular_list(input)
    head = insert_node(head, value)
    assert output == from_circular_list(head)


def test_insert_node():
    check_insertion([3, 5, 7], 4, [3, 4, 5, 7])
    check_insertion([3, 5, 7], 9, [3, 5, 7, 9])
    check_insertion([3, 5, 7], 1, [1, 3, 5, 7])
    check_insertion([3, 3, 7], 1, [1, 3, 3, 7])
    check_insertion([3, 3, 7], 3, [3, 3, 3, 7])

    check_insertion([], 1, [1])
    check_insertion([1], 3, [1, 3])
    check_insertion([5], 3, [3,5])
