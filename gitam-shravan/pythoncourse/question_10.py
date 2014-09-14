__author__ = 'Kalyan'

def left_binary_search(input, value):
    i=0
    if input is None:
        return -1
    length=0
    for element in input:
        length+=1
    start=0
    last = length -1
    found=0
    while start <= last and found ==0:
        mid=(start+last)/2
        if input[mid]==value:
            found=1
            while i<length:
                 if input[i]==input[mid] and i<mid:
                     mid=i
                 i+=1
            return mid
        elif value <input[mid]:
            last = mid-1
        elif value > input[mid]:
            start = mid+1
    if found == 0:
        return -1


def test_left_binary_search():
    input = range(10)
    for index, value in enumerate(input):
        assert index == left_binary_search(input, value)
        
    assert -1 == left_binary_search(input, -10)
    assert -1 == left_binary_search(input, 100)

    assert -1 == left_binary_search([], 10)
    assert -1 == left_binary_search(None, 10)
    assert 0 == left_binary_search([10], 10)
    assert -1 == left_binary_search([10], 5)

    input = [1,1,2,2,2,3,3,4,3]

    assert 0 == left_binary_search(input, 1)
    assert 2 == left_binary_search(input, 2)
    assert 5 == left_binary_search(input, 3)
