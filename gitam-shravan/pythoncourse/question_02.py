__author__ = 'kishore'

notes = """
   This problem is to introduce you to bit manipulations concepts and unit testing.

"""

# zero_ones is a n arbitrary iterable which returns a series of 0's or 1's
# convert it to a python long. So I could pass in a string or list or tuple or generator of 0's and 1's

def binary_to_base10(zero_ones):
    if zero_ones is None:
        return None
    iter_obj=iter(zero_ones)
    product=0
    result=[]
    try:
        while iter_obj:
            item=iter_obj.next()
            product=product*2+int(item)
            result.append(product)
    except StopIteration:
        print result
        return result

#Write tests to test your solution for all possible valid inputs
def test_binary_to_base10():
    assert [1,2,5]==binary_to_base10([1,0,1])
    assert [1,2,5]==binary_to_base10("101")
    assert [1,2,5]==binary_to_base10((1,0,1))
    assert []== binary_to_base10("")
    assert []== binary_to_base10([])
    assert []== binary_to_base10(())
    assert [1,2,5,11]== binary_to_base10(('1',0,'1','1'))
    assert None== binary_to_base10(None)
    assert 'error'==binary_to_base10('123')
    assert 'error'==binary_to_base10('abc')
    assert [1,2,5,11]==binary_to_base10(('1011'))
    assert 'error' == binary_to_base10('a1b0c2')
    assert [1,2,5] == binary_to_base10('1 0 1 ')
