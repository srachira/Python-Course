

notes = """
    This is to introduce you to create data structures of your own without help of built-in structures.
"""


#Convert a number into linked list such that each digit is in a node and pointing to node having next digit.
#The function should return head of the linked list.
#Do not use built-in functions.


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


def number_to_LinkedList(numbers):
    res=[None]*len(str(numbers))
    i=len(str(numbers))-1
    head = None
    prev = None
    while numbers>0:
        numbers1=int(numbers)%10
        res[i]=numbers1
        i-=1
        numbers=int(numbers)/10
       # print res
    for each in res:
       # print each
        node = Node(each)
        if not head:
            head= node
        elif prev!=None:
            prev.next = node
        prev = node
    #print head.value
    #print head.next.value
    #print head.next.next.value
    return head
#write down tests covering all possible cases to your solution
#Hint: Here tests can use built-in functions
def test_number_to_LinkedList():
    a=number_to_LinkedList(123)
    assert 1==a.value
    assert 2==a.next.value
    assert 3==a.next.next.value
    b=number_to_LinkedList(2456)
    assert 2==b.value
    assert 4==b.next.value
    assert 5==b.next.next.value
    assert 6==b.next.next.next.value