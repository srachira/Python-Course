__author__ = 'Kalyan'

def right_binary_search(input, value):
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
                 if input[i]==input[mid] and i>mid:
                     mid=i
                 i+=1
            return mid
        elif value <input[mid]:
            last = mid-1
        elif value > input[mid]:
            start = mid+1
    if found == 0:
        return -1


def test_right_binary_search():
    input = range(10)
    for index, value in enumerate(input):
        assert index == right_binary_search(input, value)
        
    assert -1 == right_binary_search(input, -10)
    assert -1 == right_binary_search(input, 100)

    assert -1 == right_binary_search([], 10)
    assert -1 == right_binary_search(None, 10)
    assert 0 == right_binary_search([10], 10)
    assert -1 == right_binary_search([10], 5)

    input = [1,1,2,2,2,3,3,4,3]

    assert 1 == right_binary_search(input, 1)
    assert 4 == right_binary_search(input, 2)
    assert 8 == right_binary_search(input, 3)


    assert -1 == right_binary_search([None],None)                   # None search
    assert -1 == right_binary_search([1,2,3,4,5,6,7],None)          # None key
    assert 2 == right_binary_search([-3,-3,-3,-2,-2],-3)            # Negative values
    assert "invalid data" == right_binary_search([None,None,None],0)# None list
    assert "invalid data" == right_binary_search(["abc","def","def","drug"],"def")#invalid data
    assert "invalid data" == right_binary_search([1,8,9,[10,12],[10,12]],[10,12]) #invalid data
    assert "invalid data" == right_binary_search([(1,2),(4,5),(4,5)], (4,5))      #invalid data
    assert "invalid key" == right_binary_search([1,2,3,4,5],"ROFL")  # invalid key
    assert 3 == right_binary_search([2,2,2,2,1,8,9],'2')             # valid Int as strings
