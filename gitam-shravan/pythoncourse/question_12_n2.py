__author__ = 'SuSh'
def rotate_right(input,number):
    length=len(input)
    while number:
        temp=input[-1]
        for i in range(length-1,0,-1):
            temp1=input[i]
            input[i]=input[i-1]
        input[0]=temp
        number-=1
    print input



def test_rotate():
    input = range(1,7)
    rotate_right(input, 2)
    assert [5,6,1,2,3,4] == input

    input = range(1,7)
    rotate_right(input, 3)
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
    rotate_right(input, 0)
    assert [1,2,3,4,5,6] == input