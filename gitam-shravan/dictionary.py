__author__ = 'SuSh'
import os
import inspect

def helpp():
    d = {}
    mod_file = inspect.getfile(inspect.currentframe())
    mod_dir = os.path.dirname(mod_file)
    file=os.path.join(mod_dir, 'helpp.txt')
    with open(file) as f:
        for line in f:
           (key,val,msg,email) = line.split()
           d[key] = (val,msg)
    return d


def authentication(user_name,data):
    if user_name in data.keys():
        print "Authenticated"
    else:
        print "Enter a Valid User input!"


d=helpp()
authentication('Armaan',d)