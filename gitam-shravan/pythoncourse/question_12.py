__author__ = 'Kalyan'

# rotate the input list by number times in place.
# don't use any new intermediate lists if possible.
def reverse(input,start,end,length):
    if input is None:
        return None
    index=0
    while index<(length/2):#and start is not end:
        temp=input[end]
        input[end]=input[start]
        input[start]=temp
        start+=1
        end-=1
        index+=1
    return input

def rotate_left(input, number):
    length=0
    for each in input:
        length+=1
    end=length-1
    reverse(input,0,end,length)
    reverse(input,0,number-1,(number))
    reverse(input,number,end,length-(number))
    return input

def rotate_right(input, number):
    if type(number).__name__=='str':
        return input
    if input is None:
        return None
    length=0
    for each in input:
        length+=1
    if length==0:
        return []
    if number == 0:
        return []
    number=int(number)
    if number==length or number == 0 or number < 0:
        return input
    elif number > length:
        number = number%length
        if number > length/2:
            rotate_left(input, len(input)-number)
    end=length-1
    reverse(input,0,end,length)
    reverse(input,0,number-1,(number))
    reverse(input,number,end,length-(number))
    return input



def test_rotate():

    input = range(1,7)
    rotate_right(input, -2)
    assert [1,2,3,4,5,6] == input

    input = range(1,7)
    rotate_right(input, 3.5)
    assert [4,5,6,1,2,3] == input

    input = range(1,7)
    rotate_right(input, 1)
    assert [6,1,2,3,4,5] == input

    input = range(1,7)
    rotate_right(input, 6)
    assert [1,2,3,4,5,6] == input

    input = range(1,7)
    rotate_right(input, 8)
    assert [5,6,1,2,3,4] == input

    input = range(1,7)
    rotate_right(input, 60)
    assert [1,2,3,4,5,6] == input

    input = range(1,7)
    rotate_right(input, '101')
    assert [1,2,3,4,5,6]== input

    input = None
    rotate_right(input, 101)
    assert None== input


    input = None
    rotate_right(input, None)
    assert None== input

    input = []
    rotate_right(input, [])
    assert []== input





assert [2,3,4,5,6,1] == rotate_right(range(1,7),5 ) #rotate left by 1
assert [6,1,2,3,4,5]==rotate_right(range(1,7), 1)
assert [1,2,3,4,5,6] == rotate_right(range(1,7), 6) #No rotations since range is equal to number of rotations
assert [1,2,3,4,5] == rotate_right(range(1,6), 100) # Shouldn't rotate since len(input)%number=0
assert range(3,601)+[1,2] == rotate_right(range(1,601), 598) # rotate left by 2
assert [5,6,1,2,3,4] == rotate_right(range(1,7), 8)
assert [1,2,3,4,5,6] == rotate_right(range(1,7), -8) #no. of rotations as negative number
assert [] == rotate_right([], 8)#empty list as input
assert None == rotate_right(None, 2)#Input is None
assert [1,2,3,4,5,6] == rotate_right(range(1,7), None) #no. of rotations

assert [1,2,3,4,5,6]==rotate_right(range(1,7), '1') #String type are not accepted
assert [1,2,3,4,5,6]==rotate_right(range(1,7), 1.2)#Float types are not accepted
assert [1,2,3,4,5,6]==rotate_right(range(1,7), 2.5)






