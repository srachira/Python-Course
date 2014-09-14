__author__ = 'SuSh'
import os
import inspect
import glob

def get_file_path(file):
    mod_file = inspect.getfile(inspect.currentframe())
    mod_dir = os.path.dirname(mod_file)
    return os.path.join(mod_dir, file)

def create_file(filename,message):
    f=open(filename,"a")
    f.write("{0}\n".format(message))
    f.close()

def open_file(filename):
    mod_file = inspect.getfile(inspect.currentframe())
    mod_dir = os.path.dirname(mod_file)
    file=os.path.join(mod_dir, filename)
    f=open(file,"rt")
    c = ""
    no=1
    while True:
        for i in f.readlines():
            c = c + str(no) +'.' + i
            no+=1
        break
    f.close()
    return c

def view_all():
    c=''
    mod_file = inspect.getfile(inspect.currentframe())
    mod_dir = os.path.dirname(mod_file)
    os.chdir(mod_dir)
    i=1
    while True:
        for files in glob.glob("*.txt"):
            c= c + str(i) + '.'+ files + "\n"
            i+=1
        break
    return c

def write_file(filename,msg):
    mod_file = inspect.getfile(inspect.currentframe())
    mod_dir = os.path.dirname(mod_file)
    file=os.path.join(mod_dir, filename)
    with open(file,"a") as f:
        f.write(msg)
    f.close()

def write_answer():
    view_all()
    return
