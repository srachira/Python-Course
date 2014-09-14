__author__ = 'Kalyan'

notes = '''
Python has a good api to deal with text and binary files. We explore that
in this module.

Use help(file.XXX) to find help on file method XXX (tell, seek etc.)
'''

from placeholders import *

#opens a file from the module directory.
def open_test_file(file, mode="rt"):
    import inspect, os.path
    mod_file = inspect.getfile(inspect.currentframe())
    mod_dir = os.path.dirname(mod_file)
    test_file = os.path.join(mod_dir, file)
    return open(test_file, mode)


def test_file_readlines():
    f = open_test_file("test_file.txt")
    lines = f.readlines()
    assert ['one\n', 'two\n', 'three\n', 'four\n', 'five\n'] == lines


def test_file_read():
    f = open_test_file("test_file.txt")
    data = f.read()
    assert 'one\ntwo\nthree\nfour\nfive\n' == data


def test_file_end():
    f = open_test_file("test_file.txt")
    s = f.read() # read till end.
    assert '' == f.read()
    assert '' == f.read()


def test_file_read_binary():
    f = open_test_file("test_file.txt", "rb")
    lines = f.readlines()
    assert ['one\r\n', 'two\r\n', 'three\r\n', 'four\r\n', 'five\r\n'] == lines
    f.seek(0, 0)
    data = f.read()
    assert 'one\r\ntwo\r\nthree\r\nfour\r\nfive\r\n' == data


def test_file_windows_newlines():
    f = open_test_file("newlines_tmp.txt", "wb")
    f.write("one\r\ntwo\rthree\n")
    f.close()

    f = open_test_file("newlines_tmp.txt", "rt")
    assert 'one\ntwo\rthree\n' == f.read()
    f.close()

    f = open_test_file("newlines_tmp.txt", "rb")
    data = f.read()
    assert '' == f.read()

    #windows behavior : http://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files


def test_file_universal_newlines():
    f = open_test_file("newlines_tmp.txt", "wb")
    f.write("one\r\ntwo\rthree\n")
    f.close()

    f = open_test_file("newlines_tmp.txt", "rU")
    assert 'one\ntwo\nthree\n' == f.read()
    assert ('\r', '\n', '\r\n') == f.newlines


def test_file_readline():
    f = open_test_file("test_file.txt")
    lines = []
    while True:
        line = f.readline()
        if not line:
            break
        lines.append(line)

    assert ['one\n', 'two\n', 'three\n', 'four\n', 'five\n'] == lines


def test_file_iteration():
    f = open_test_file("test_file.txt")
    lines = []
    for x in f:
        lines.append(x)
    assert ['one\n', 'two\n', 'three\n', 'four\n', 'five\n'] == lines


def test_file_tell():
    tells = []
    f = open_test_file("test_file.txt")
    while True:
        line = f.readline()
        tells.append(f.tell())
        if not line:
            break
    assert [5L, 10L, 17L, 23L, 29L, 29L] == tells


def test_file_readlines_tell():
    tells = []
    f = open_test_file("test_file.txt")
    for line in f.readlines():
        tells.append(f.tell())

    assert [29L, 29L, 29L, 29L, 29L] == tells


def test_file_iteration_tell():
    tells = []
    f = open_test_file("test_file.txt")
    for line in f:
        tells.append(f.tell())

    assert [29L, 29L, 29L, 29L, 29L] == tells # is there really no difference between readlines and iteration?
   #Readlines was there way before file objects were iterable. So it is there for backward compatibility.
#The difference between readlines and iteration in files is that readlines reads a bunch of data at a time
# readlines[size] where as using iterators we can scan line by line. :)


def test_file_seek():
    f = open_test_file("test_file.txt")
    assert 0L == f.tell()
    f.read()
    assert 29L == f.tell()
    assert '' == f.read()

    f.seek(0, 0)
    assert 'one\ntwo\nthree\nfour\nfive\n' == f.read()
    f.seek(-3, 2)
    assert 'e\n' == f.read()
    f.seek(-2, 1)
    assert '\n' == f.read()

#windows has a few newlines quirks.
def test_file_write_text():
    f = open_test_file("test_write.txt", "w") # same as "wt"
    f.write("one\ntwo\nthree\n")
    f.close()

    f = open_test_file("test_write.txt", "rb")
    assert 'one\r\ntwo\r\nthree\r\n' == f.read()

    f = open_test_file("test_write.txt", "rt")
    assert 'one\ntwo\nthree\n' == f.read()


def test_file_write_binary():
    f = open_test_file("test_write.txt", "wb")
    f.write("one\ntwo\nthree\n")
    f.close()

    f = open_test_file("test_write.txt", "rb")
    assert 'one\ntwo\nthree\n' == f.read()

    f = open_test_file("test_write.txt", "rt")
    assert 'one\ntwo\nthree\n' == f.read()


# It is generally a good practice to close files after their use is over
def test_file_close():
    f = open_test_file("test_file.txt")
    assert False == f.closed
    try:
        lines = [line.strip() for line in f.readlines()]
    finally:
    # putting it in finally so that it is closed even if an exception is raised
        f.close()
    assert True == f.closed

# http://effbot.org/zone/python-with-statement.htm
def test_with_statement():
    try:
        with open_test_file("test_file.txt") as f:
            assert False == f.closed
            raise Exception("some random exception")
    except Exception as ex:
        print ex
        pass

    assert True == f.closed


three_things_i_learnt = """
-Files are iterable.Modes in files are read,append,write. We add "b" for binary mode,
"+" to allow simultaneous reading and writing.
-We add a "U" to mode to open file for input with a Universal newline.
-Any line ending in the input wil be seen as "\n".
-tell() is used to indicate the current file position (in LONG).
-read([size]) reads at most size bytes and returned as a string.
-readlines([size]) reads a bunch of lines in a file.
-write(str)- used to write str to a file.
-writelines(seq_of_str)- used to write a sequence of str into a file.
-seek() is used to move to a file position.
-close is used to close a file.
-closed-- returns true if the file is closed. :)
"""

time_taken_minutes = 30
