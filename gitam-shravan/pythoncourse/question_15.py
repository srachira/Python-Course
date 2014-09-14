__author__ = 'Kalyan'

notes = '''
This problem deals with circular single linked lists, the tail of the list points back to head.
'''

from listutils import *


# delete a node in the list so that the resulting list is still circular.
def delete_node(head, value):
    p=head
    if p is None:
        return None
    while p.value!=value:
        p=p.next
        if p.next is head and p.value!=value:
            return head
    if p.next is p:
        return None
    else:
        p.value=p.next.value
    if p.next==head:
        head=p
    p.next=p.next.next
    return head


def check_deletion(input, value, output):
    head = to_circular_list(input)
    head1= delete_node(head, value)
    assert output == from_circular_list(head1)

def test_delete_node():
    check_deletion(range(1,6), 1, range(2,6))
    check_deletion(range(1,6), 5, range(1,5))
    check_deletion(range(1,6), 3, [1,2,4,5])
    check_deletion(range(1,6), 4, [1,2,3,5])
    check_deletion(range(1,6), 10, range(1,6))
    check_deletion([1], 10, [1])
    check_deletion([1,1], 1, [1])
    check_deletion([1], 1, [])
    check_deletion([1,2,3], 2, [1,3])
    check_deletion([], None, [])


