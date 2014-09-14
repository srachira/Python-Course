__author__ = 'Kalyan'

notes = '''
This assignment covers file io and data generation. Actually open the files and check if they are as expected.
'''
import os
import inspect

from placeholders import *


# Create a text file with name filename and about size bytes. The file should contain
# an incrementing number on each line starting with 0. (ie) 0, 1, 2, 3, .... as many are required to make the file size
# just >= size. Each line should end with windows newline ("\r\n").
def create_file_numbers(filename, size):
    max_size = long(size)
    file_name = filename
    f = file(file_name, "wb")
    i = 0
    while True:
        if f.tell() <= max_size:
            f.write((str(i))+'\r\n')
            i += 1
        else:
            f.close()
            break


def check_file_size(file_path, size):
    assert os.stat(file_path).st_size >= size, "Size not correct"
    f = open(file_path, "rb")
    f.seek(size, 0)
    extra = f.read()
    assert extra.count("\r\n") <= 1, "too many extra lines"


def check_file_contents(file_path):
    expected_value = 0
    for line in open(file_path, "rb"):
        assert line.endswith("\r\n")
        assert not line.endswith("\r\r\n")
        assert expected_value == int(line)
        expected_value += 1


def check_file(file_path, size):
    check_file_size(file_path, size)
    check_file_contents(file_path)


def test_create_file_numbers():
    file1k = get_file_path("1k_numbers.txt")
    create_file_numbers(file1k, 1024)
    check_file_size(file1k, 1024)
    check_file_contents(file1k)

    file1M = get_file_path("1M_numbers.txt")
    create_file_numbers(file1M, 1024 * 1024)
    check_file_size(file1M,  1024 * 1024)
    check_file_contents(file1M)

#utility function which returns a full path which is (currentmoduledir + file), useful to generate temporary files in
# in the same directory as the module without worrying about the current path set by pycharm etc.
def get_file_path(file):
    mod_file = inspect.getfile(inspect.currentframe())
    mod_dir = os.path.dirname(mod_file)
    return os.path.join(mod_dir, file)


three_things_i_learnt = """
-Creating files opening and writing into files.
-Writing into files of specific size. This can be done by calculating the position in the file
using tell before inserting a string into the file.
-Only string types can be inserted into a file.. Integers have to be converted to
strings before inserting them into a file. :)
"""

time_taken_minutes = 90
