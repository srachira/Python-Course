__author__ = 'hemavishnu'

notes = """
    This is to refresh your bit manipulation skills.
"""


#Convert integer to binary string and return the string.
#Integers also include negative numbers. So for negative numbers represent in two's complement.
#Integers are 32-bit integers.
def integer_to_binary(input):
    if (isinstance(input,int))==False:
        print "Enter a valid integer"
        return None

    mask=1<<31
    i=0
    complement=""
    while i<32:
        if (mask&input):
            complement+='1'
        else:
            complement+='0'
        input=input<<1
        i+=1
    return complement


#write tests to test your solution
def test_integer_to_binary():
    assert '00000000000000000000000000001010' == integer_to_binary(10)
    assert '00000000000000000000000001111101' == integer_to_binary(125)
    assert '11111111111111111111111010100011' == integer_to_binary(-349)
    assert '00000000000000000000000000000000' == integer_to_binary(0)
    assert '00000000000011110100001001000000' == integer_to_binary(1000000)
    assert '11111111111111111111111111111111' == integer_to_binary(-1)
    assert '11111111111100001011110111000000' == integer_to_binary(-1000000)
    assert '00000000000000000000000000011000' == integer_to_binary(24)
    assert '01111111111111111111111111111111' == integer_to_binary(2147483647)
    assert '10000000000000000000000000000000' == integer_to_binary(-2147483648)
    assert '10000000000000000000000000000001' == integer_to_binary(-2147483647)
    assert None == integer_to_binary("dsfj")
    assert None == integer_to_binary((1,2,3))
    assert None == integer_to_binary([3,4,5])
    assert None == integer_to_binary(None)
    assert None == integer_to_binary(36.283)
    assert None == integer_to_binary(68719476735)

