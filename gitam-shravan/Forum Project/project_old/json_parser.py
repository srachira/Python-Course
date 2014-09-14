__author__ = 'Vineeth'

input_set = ['''
{"forum1": {'category1': [2, [1, 'q1'], [2, 'q2']], 'category2': [
            2, [1, 'q3'], [2, 'q4']]}, 'forum2': {"category3": [2, [1, "q5"], [2, "q6"]],
                                                  "category4": [2, [1, "q7"], [2, "q8"]]}}

''']

def get_string(input, index):
    string = ''
    while input[index] != '"' and input[index] != "'":
        string += input[index]
        index += 1
    return string, index + 1

def get_number(input, index):
    num_string = ''
    while input[index] != ':' and input[index] != ',' and input[index] != '}':
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
        elif input[index] == '[':
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
    while input[index] != ']':
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


def convert_to_json_object(input):
    i, length = 0, len(input)
    json_dict = None
    while i < length:
        if input[i] == '{':
            json_dict, i = get_dict(input, i + 1)
        else:
            i += 1
    return json_dict



if __name__ == '__main__':
    a = convert_to_json_object(input_set[0])
    print a
    print len(a)