from bottle import route, run, request, get, post, response

forumsDict = dict()

@route('/hello')
def gethello():
    return "Hello World!"

@route('/forums')
def getForums():
     return "forum1,forum2"

@route('/forums', method='POST')
def addForum():
    data1 = request.POST['forumname']
    data2 = request.POST['createdby']

    return data1 + ' created'


@route('/forums/forum/<forumname>')
def getForum(forumname):
    return forumname + " Messages: msg1"

run(host='localhost', port=8080, debug=True, reloader=True)

