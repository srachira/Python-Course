__author__ = 'Kalyan'

from listutils import *


def merge_lists(head1, head2):
    current=head1
    count=0
    while current is not None and current.next is not None:
        current=current.next
        count+=1
    else:
        if current is None:
            current=head2
        else:
            current.next=head2
    current = head1
    while current is not None and current.next is not None:
        counter=current.next
        while counter.next is not None:
            if current.value > counter.value:
                temp = current.value
                current.value = counter.value
                counter.value = temp
            counter=counter.next
        current=current.next
    else:
        if current is None:
            return head2
        else:
            return head1

def test_merge_lists():
    head1 = to_linked_list([1, 2, 3])
    head2 = to_linked_list([1, 2, 3, 4, 5])

    result = merge_lists(head1, head2)
    assert [1, 1, 2, 2, 3, 3, 4, 5] == from_linked_list(result)

    head1 = to_linked_list([1, 2, 5])
    head2 = to_linked_list([4, 6, 7])

    result = merge_lists(head1, head2)
    assert [1, 2, 4, 5, 6, 7] == from_linked_list(result)

    head1 = to_linked_list([])
    head2 = to_linked_list([1, 2, 3, 4])

    result = merge_lists(head1, head2)
    assert [1, 2, 3, 4] == from_linked_list(result)

    result = merge_lists(None, None)
    assert [] == from_linked_list(result)

    head1 = to_linked_list([1,2,3,4,5,6,7,8,9,10])
    head2 = to_linked_list([1, 2, 3, 4,5,6,7,8,9,10])

    result = merge_lists(head1, head2)
    assert [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10] == from_linked_list(result)

    head1 = to_linked_list([])
    head2 = to_linked_list([1, 2, 3, 4,5,6,7,8,9,10])

    result = merge_lists(head1, head2)
    assert [1, 2, 3, 4,5,6,7,8,9,10] == from_linked_list(result)









