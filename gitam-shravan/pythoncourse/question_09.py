__author__ = 'Kalyan'


def binary_search(input, key):
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
        if input[mid]==key:
            found=1
            return mid
        elif key <input[mid]:
            last = mid-1
        elif key > input[mid]:
            start = mid+1
    if found ==0:
        return -1



def test_binary_search():
    input = range(10)
    for index, value in enumerate(input):
        assert index == binary_search(input, value)

    assert -1 == binary_search(input, -10)
    assert -1 == binary_search(input, 100)

    assert -1 == binary_search([], 10)
    assert -1 == binary_search(None, 10)
    assert 0 == binary_search([10], 10)
    assert -1 == binary_search([10], 5)


