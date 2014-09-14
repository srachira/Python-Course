__author__ = 'Kalyan'

notes = '''
Continuing on our theme of actually measuring how long our programs take, I would like you use the code below to
understand profiling in python.

Using time.clock() will be sufficient if you are looking at method level granularity. But if you are looking to dig deeper
using it before and after every suspect line is tedious. For such scenarios profilers are very useful to give you a clear
idea of where your program is spending time.

Read up on the cProfile module at http://docs.python.org/2/library/profile.html and use it on this on the
create_file_numbers_old and figure out the main bottleneck. Rewrite create_file_numbers_new to address this bottleneck
to get at least 5-10 times speed up.
'''

import functools
import cProfile
import inspect
import os
import sys
import time

def create_file_numbers_old(filename, size):
    start = time.clock()
    value = 0
    with open(filename, "w") as f:
        while f.tell()< size:
            f.write("{0}\n".format(value))
            value += 1

    end = time.clock()
    print "time taken to write a file of size", size, " is ", (end -start), "seconds \n"


def create_file_numbers_new(filename, size):
    start = time.clock()
    value = 0
    length = 0 # number of bytes written so far
    with open(filename, "w") as f:
        while length < size-3:
            s = str(value) + '\n'
            length += len(s) + 1 # add how many bytes are in this write()
            f.write(s)
            value += 1


    end = time.clock()
    print "time taken to write a file of size", size, " is ", (end -start), "seconds \n"

#create_file_numbers_new= memorize(create_file_numbers_new)


def get_module_dir():
    mod_file = inspect.getfile(inspect.currentframe())
    return os.path.dirname(mod_file)

output_path = functools.partial(os.path.join, get_module_dir())

#pass file name and size from command line
def main(argv = sys.argv):
    #add argument checking and parsing here ..

    fpath = output_path(r"est.txt")
    size=50*1024*1024
    cProfile.run("create_file_numbers_old('%s', %d)" %(fpath, size))
    fpath1 = output_path(r"est1.txt")
    cProfile.run("create_file_numbers_new('%s', %d)" %(fpath1, size))


if __name__ == "__main__":
    main()


my_analysis = '''
Using cProfile i've found that that the code spends most of it's time in performing the write and tell methods.
The tell method tells where we actually are i.e the position in the file and the write method is used to write into
the file. Both the methods are costly, both are them need to be reduced i.e we need to optimize this part of the code

                                         while f.tell() <= size:
                                            try:
                                              f.write("{0}\n".format(value))
                                              i+=1
                                            except f.tell() > size:
                                              f.close()

The while part where we spend most of the time in checking the position and writing into a file. So, to reduce this we
use the length.. i.e calculating the length based on which we write into a file.
The while loop may be optimized by using the loop optimization techniques i.e using two write statements into a single
loop and reduce the repetitions. And because of rewriting the loop, we can get into a good runtime.
Instead of tell() we can use a variable which calculates the length of the string before inserting and
when the size reaches a limit we specified we stop and close the file.
The cProfile is used to find out where most of the time is spent during running of the program. It helps to find where
actually the code is slow! cProfile.run() gives the stats of the program under execution.
It actually helps us in optimizing the code, because when we know where we are actually lagging we can try to
optimize it.

'''