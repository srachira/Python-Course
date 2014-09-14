__author__ = 'kishore'

notes = """
    This is to introduce you to think on optimizing the solution by iterating down the code written
"""


#Given a list of numbers, modify the list so that each element has the product of all elements except the number
#ex: Input:[1,2,3,4,5]
#output:[120,60,40,30,24]
#Return the list of products

def product_of_list_elements(numbers):

    if len(numbers) == 1:
        return numbers
    if len(numbers) is 0:
        return []
    else:
        length=0
        product=1
        for i in numbers:
            length+=1
        LMA=[None]*length
        j=length-1
        while j>=0:
            product*=numbers[j]
            LMA[j]=product
            j-=1
        product=1
        i=0
        while i<length-1:
            LMA[i]=product*LMA[i+1]
            product*= numbers[i]
            i+=1
        LMA[i]=product

    return LMA

#write your own tests covering all the possible cases to your solution
def test_product_of_list_elements():
    assert [120,60,40,30,24]==product_of_list_elements([1,2,3,4,5])
    assert [0,0,0,30,0]==product_of_list_elements([1,2,3,0,5])
    assert [0,0,0,0,0]==product_of_list_elements([1,0,3,0,5])
    assert [-12,6,-4,-6]==product_of_list_elements([1,-2,3,2])
    assert product_of_list_elements([1,2,4,5,6]) == [240, 120, 60, 48, 40] # Normal input
    assert product_of_list_elements([4]) == [4] # To check for unit sized list
    assert product_of_list_elements([1,4,0,2,7]) == [0, 0, 56, 0, 0] # With zero
    assert product_of_list_elements([]) == [] # Empty list
    assert product_of_list_elements([-1,2,4,5,6]) == [240, -120, -60, -48, -40] #With negative numbers
    assert product_of_list_elements([1.2, 1.2]) == [1.2,1.2] # Float values
    assert product_of_list_elements([1.7,1.1,1]) == [1.1, 1.7, 1.87] #Float values
    assert product_of_list_elements([0.3,0.3]) == [0.3,0.3] #Float Values
    assert product_of_list_elements([1/3,1,2.0]) == [2.0, 0.0, 0] #Rational numbers (remember 1/3 = 0)
    assert product_of_list_elements([1.0/3,1,2.0]) == [2.0,2.0/3,1.0/3] # Explicitly mentioned rational
    assert product_of_list_elements([1.2,1.1,3]) == [3.3000000000000003, 3.5999999999999996,1.32] #This case is exceptional as it is # machine specific. It may not run the same output on all machines. The issue is with the machine implementation of recursive nature of # the floating point






