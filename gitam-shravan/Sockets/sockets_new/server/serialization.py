__author__ = 'pranee'
import string

def convert_list(input_set):
    dict={}
    i,length=0,len(input_set)
    while i < length:
        dict[input_set[i][0]]= input_set[i][1]
        i=i+1
    return str(dict)
convert_list()