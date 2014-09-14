__author__ = 'SuSh'

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

def rotate_right_gcd(input,number):
    length=0
    for each in input:
        length+=1
    if number==length or number == 0:
        return input
    elif number > length:
        number = number-length
    next_temp = []
    prev_temp = []
    count = 0
    start_index = length - number
    gcd1 = gcd(start_index,number)
    while gcd1 != 0:
        next_index = (number + start_index) % length
        index = start_index
        while next_index != start_index:

                next_index = (number + index) % length
                prev_temp = next_temp
                next_temp = input[next_index]
                if count == 0:
                    count = 1
                    input[next_index] = input[start_index]
                    index = next_index
                else:
                    input[next_index] = prev_temp
                    index = next_index
        gcd1-= 1
        start_index += 1
        count = 0
    return input

def test_rotate():
    input = range(1,7)
    rotate_right_gcd(input, 2)
    assert [5,6,1,2,3,4] == input

    input = range(1,7)
    rotate_right_gcd(input, 3)
    assert [4,5,6,1,2,3] == input

    input = range(1,7)
    rotate_right_gcd(input, 1)
    assert [6,1,2,3,4,5] == input

    input = range(1,7)
    rotate_right_gcd(input, 6)
    assert [1,2,3,4,5,6] == input

    input = range(1,7)
    rotate_right_gcd(input, 8)
    assert [5,6,1,2,3,4] == input


