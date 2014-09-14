__author__ = 'Kalyan'


import inspect
import os
import time


def create_file_numbers_1(filename, size):
    value = 0
    with open(filename, "w") as f:
        while f.tell()< size:
            f.write("{0}\n".format(value))
            value += 1

def create_file_numbers_2(filename, size):
    f = open(filename,"wb")
    s=''
    p=0
    while len(s)<=size:
        s=s+str(p)+'\r\n'
        p+=1
    f.write(s)

#utility function which returns a full path which is (currentmoduledir + file), useful to generate temporary files in
# in the same directory as the module without worrying about the current path set by pycharm etc.
def get_file_path(file):
    mod_file = inspect.getfile(inspect.currentframe())
    mod_dir = os.path.dirname(mod_file)
    return os.path.join(mod_dir, file)


if __name__ == "__main__":
    # for x in [1, 1024, 10 * 1024]:
    for x in [1024]:
        filename = "{0}_k.txt".format(x)
        filepath = get_file_path(filename)
        start = time.clock()
        create_file_numbers_1(filepath ,  x*1024)
        end = time.clock()
        print "It took {0} seconds to write a file {1}".format((end-start),filename)


