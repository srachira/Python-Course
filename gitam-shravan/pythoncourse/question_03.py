__author__ = 'kishore'

notes = """
    This is to make you familiar with in place usage of lists.
"""


#numbers is list of 0's 1's and 2's ina random order.
#Your job is to modify the list in place to sort in increasing order
#Don't use any builtin functions on lists

def sort_0_1_2(numbers):
    length=0
    for i in numbers:
        length+=1
    j=length-1
    k=2
    i=0
    while k>0:
        i=0
        while i<j:
            if numbers[i]==k:
                numbers[i]=numbers[j]
                numbers[j]=k
                j-=1
                i+=1
            elif numbers[j]==k:
                j-=1
            else:
                i+=1

        k-=1
    return numbers


#write tests to test your solution.
def test_sort_0_1_2():
    assert [0,0,0,0,1,1,1,1,2]==sort_0_1_2([0,1,2,0,1,0,1,1,0])
    assert [1,1,1,1]==sort_0_1_2([1,1,1,1])
    assert [0,0,0,0]==sort_0_1_2([0,0,0,0])
    assert [2,2,2,2]==sort_0_1_2([2,2,2,2])
    assert [1,1,1,2,2]==sort_0_1_2([1,1,1,2,2])