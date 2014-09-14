__author__ = 'Kalyan'

notes = '''
This problem deals with circular linked lists. The circular list is sorted, but the head does not point to the lowest
element, it can point to a random element.
'''

from listutils import *

# insert into a sorted linked list so that the resulting list is still sorted. head does *NOT* point to the minimum node.
# do not modify head unless required.
def new_node(head,value):
    new=Node(value)
    if head is not None:
        p=head
        p1=head.next
        temp= None
        while True:
            if p != p1:
                if (p.value < value) and (p1.value >= value):
                    p.next = new
                    new.next = p1
                    break
            if p == p1:
                if p.value >= value:
                    p.next = new
                    new.next = p
                else:
                    p.next = new
                    new.next = p
                break
            if p1 == head:
                if p.value < value:
                    p.next = new
                    new.next = p1
                if p1.value >= value:
                    p.next = new
                    new.next = p1
                break
            p=p.next
            p1=p1.next


def insert_sorted(head, value):
    if head is not None:
        p=head
        p1=head.next
        temp= None
        while True:
            if p.value > p1.value:
                temp=p1
                break
            if p1 is head:
                break
            p=p.next
            p1=p1.next
        if temp is None:
            new_node(head,value)
        else:
            new_node(temp,value)
        return head
    else:
        head = Node(value)
        head.next = head
        return head


def check_insertion(input, value, output):
    head = to_circular_list(input)
    head = insert_sorted(head, value)
    assert output == from_circular_list(head)



def test_insert_sorted():
    check_insertion([11, 13, 5, 7, 9], 15, [11,13, 15, 5, 7, 9])
    check_insertion([11, 13, 5, 7, 9], 10, [11, 13, 5, 7, 9, 10])
    check_insertion([11, 13, 5, 7, 9], 3, [11, 13, 3,  5, 7, 9])
    check_insertion([11, 13, 5, 7, 9], 6, [11, 13,  5, 6, 7, 9])

    check_insertion([5], 10, [5,10])
    check_insertion([5], 1, [5,1])
    check_insertion([], 10, [10])
    check_insertion([5, 8], 7, [5,7,8])

