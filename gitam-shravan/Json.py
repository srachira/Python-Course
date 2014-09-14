__author__ = 'SuSh'
import time

input1="""
        {
            "id": 1,
            "age": 31,
            "first_name": "Arianna",
            "last_name": "Cramer",
            "height": 5.1,
            "phone_numbers": {
                "Home": "846-410-3280",
                "Fax": "854-594-3008"
            }
        },
        {
            "id": 2,
            "age": 24,
            "first_name": "Valeria",
            "last_name": "Freeman",
            "height": 5,
            "phone_numbers": {
                "Home": "853-408-2269",
                "Fax": "819-424-2056"
            }
        },
        {
            "id": 3,
            "age": 38,
            "first_name": "Gabriella",
            "last_name": "Davidson",
            "height": 5.7,
            "phone_numbers": {
                "Home": "885-526-2935",
                "Fax": "848-544-3963"
            }
        },
        {
            "id": 4,
            "age": 34,
            "first_name": "Amelia",
            "last_name": "Hoggarth",
            "height": 7.5,
            "phone_numbers": {
                "Home": "896-499-3747",
                "Fax": "812-513-2627"
            }
        },
        {
            "id": 5,
            "age": 36,
            "first_name": "Natalie",
            "last_name": "Youmans",
            "height": 7.1,
            "phone_numbers": {
                "Home": "849-576-3165",
                "Fax": "800-497-3296"
            }
        },
        {
            "id": 6,
            "age": 29,
            "first_name": "Elizabeth",
            "last_name": "Day",
            "height": 5.1,
            "phone_numbers": {
                "Home": "845-513-3400",
                "Fax": "868-415-3724"
            }
        },
        {
            "id": 7,
            "age": 30,
            "first_name": "Claire",
            "last_name": "Daniels",
            "height": 5.1,
            "phone_numbers": {
                "Home": "830-499-2912",
                "Fax": "886-586-2110"
            }
        },
        {
            "id": 8,
            "age": 34,
            "first_name": "Alyssa",
            "last_name": "Stanley",
            "height": 4.5,
            "phone_numbers": {
                "Home": "829-559-2557",
                "Fax": "897-406-3882"
            }
        },
        {
            "id": 9,
            "age": 22,
            "first_name": "Morgan",
            "last_name": "Brooks",
            "height": 6.2,
            "phone_numbers": {
                "Home": "838-436-3921",
                "Fax": "863-591-2399"
            }
        },
        {
            "id": 10,
            "age": 32,
            "first_name": "Savannah",
            "last_name": "Ward",
            "height": 5.8,
            "phone_numbers": {
                "Home": "807-534-3783",
                "Fax": "809-449-2939"
            }
        }"""



def get_string(input, index):
    string = ''
    while input[index] != '"' and input[index] != "'":
        string += input[index]
        index += 1
    return string, index + 1

def get_number(input, index):
    num_string = ''
    while input[index] != ':' and input[index] != ',' and input[index] != '}' and input[index] != ')' :
        num_string += input[index]
        index += 1
    num_string = num_string.replace(' ', '')
    return float(num_string), index

def get_dict(input, index):
    dict_gen = {}
    key, value, quote_hit, val = None, None, False, None
    while input[index] != '}':
        if input[index] == '"' or input[index] == "'":
            val, index = get_string(input, index+1)
            if quote_hit:
                value = val
            else:
                key = val
        elif input[index] in "0123456789":
            val, index = get_number(input, index)
            if quote_hit:
                value = val
            else:
                key = val
        elif input[index] == '[' or input[index] == '(':
            val, index = get_array(input, index+1)
            if quote_hit:
                value = val
            else:
                key = val
        elif input[index] == ',':
            quote_hit = False
            dict_gen[key] = value
            index += 1
        elif input[index] == ':':
            quote_hit = True
            index += 1
        elif input[index] == '{':
            val, index = get_dict(input, index + 1)
            if quote_hit:
                value = val
            else:
                key = val
        else:
            index += 1
    if key is not None and value is not None:
        dict_gen[key] = value
    return dict_gen, index + 1

def get_array(input, index):
    array_gen = []
    while input[index] != ']' and input[index]!= ')':
        if input[index] == '"' or input[index] == "'":
            val, index = get_string(input, index + 1)
            array_gen.append(val)
        elif input[index] == '[':
            val, index = get_array(input,index + 1)
            array_gen.append(val)
        elif input[index] in "0123456789":
            val, index = get_number(input, index)
            array_gen.append(val)
        elif input[index] == '{':
            dict_return, index = get_dict(input, index + 1)
            array_gen.append(dict_return)
        else:
            index += 1
    return array_gen, index + 1


def serialization(input):
    print "1"
    i, length = 0, len(input)
    list_json=[]

    json_dict = None
    while i < length:
        if input[i] == '{':
            json_dict, i = get_dict(input, i + 1)
            list_json.append(json_dict)
        else:
            i += 1
    return list_json

def main():

    result=serialization(input1)
    print result
    length=0
    for i in result:
        length+=1
    print "Length of input is:",length
    return (result,length)

def avg_age(result,length):
   add=0
   count=0
   for i in range(length):
       if result[i]["age"] >0 and result[i]["age"] < 150:
            add += result[i]["age"]
            count+=1
   average_age=add/count
   print "Average age is:",average_age

def sort_median(median,length):
    for i in range(0,length):
         for j in range(0,length-1):
             if median[j]>median[j+1]:
                    temp=median[j]
                    median[j]=median[j+1]
                    median[j+1]=temp
    return median

def median_height(result,length):
    median=[None]*length
    count=0
    for i in range(length):
        if result[i]["height"] > 0:
            median[i]=result[i]["height"]
            count+=1
    median_sorted= sort_median(median,count)#sort function
    middleValue = count / 2
    if count % 2 == 1:
        print "Median is:",median_sorted[middleValue]
    else:
        print "Median is:",(median_sorted[middleValue] + median_sorted[middleValue - 1]) / 2

def duplicate_numbers(result,length):

    for i in range(length):
        for j in range(i+1,length):
            for each in result[i]['phone_numbers']:
                if result[i]['phone_numbers'][each]== result[j]['phone_numbers'][each]:
                    print "Duplicates are:","\n",each,":",result[i]['phone_numbers'][each], result[i]['first_name'],\
                            result[i]['last_name'],"\n",each,":",result[j]['phone_numbers'][each],\
                            result[j]['first_name'],result[j]['last_name']



def contains_digits(result,length):
    i=0
    for i in range(length):
        count=0
        for char in result[i]['phone_numbers']['Home']:
            if char in '0123456789':
                count+=1
        if count is not 10:
            print 'Error in number', result[i]['phone_numbers']['Home']



if __name__=="__main__":
    a,b = main()
    tic=time.clock()
    median_height(a,b)
    toc=time.clock()
    print toc-tic
    tic=time.clock()
    avg_age(a,b)
    toc=time.clock()
    print toc-tic
    tic=time.clock()
    duplicate_numbers(a,b)
    toc=time.clock()
    print toc-tic
    tic=time.clock()
    contains_digits(a,b)
    toc=time.clock()
    print toc-tic

