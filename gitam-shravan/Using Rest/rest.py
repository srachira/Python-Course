from bottle import route, run, request, get, post, response
from File_Operations import *
forumsDict = dict()


@route('/hello')
def gethello():
    return "Hello World!"

@route('/forums')
def getForums():
    c=view_all()
    return c

@route('/forums', method='POST')
def addForum():
    data1 = request.POST['forumname']
    data2 = request.POST['message']
    filename="{0}_forum.txt".format(data1)
    filepath = get_file_path(filename)
    create_file(filepath,data2)


@route('/forums/forum/<forumname>')
def getForum(forumname):
    filename = "{0}_forum.txt".format(forumname)
    filepath = get_file_path(filename)
    c=open_file(filepath)
    return c

run(host='localhost', port=8080,debug=True, reloader=True)
