__author__ = 'hemavishnu'

notes = """
    This is to introduce you with more familiarity with linked lists
"""


class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None


def to_linked_list(plist):
    head = None
    prev = None
    for element in plist:
        node = Node(element)
        if not head:
            head = node
        else:
            prev.next = node
        prev = node
    return head


def from_linked_list(head):
    result = []
    while head:
        result.append(head.value)
        head = head.next
    return result


def to_circular_list(plist):
    head = None
    tail = None
    flag=0
    if plist is []:
        flag=1
        return None
    if plist is None :
        return None

    else:
        if flag==0 and plist!=[]:
            for element in plist:
                node = Node(element)
                if not head:
                    head = node
                else:
                    tail.next = node
                tail = node
            tail.next = head
            return head


def from_circular_list(head):
    result = []
    if head is None:
        return result;

    counter = 0 #to catch infinite loops.
    temp = head
    result.append(head.value)
    while temp.next != head and counter < 100:
        temp = temp.next
        result.append(temp.value)
        counter += 1

    return result