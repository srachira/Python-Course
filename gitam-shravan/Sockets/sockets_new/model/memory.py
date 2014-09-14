__author__ = 'Dixith Kurra'

import project13_forums.server.server
cache={}

def sign_up(data):
    try:
        assert not data.username in cache.keys()
        return insert(data)

    except AssertionError as ae:
        return False# "username already exists"

def insert(data):
    cache[data.username]=[data.password,data.email,data.DOB]
    return True
def sign_in(data):
    if data.username in cache.keys() and data.password==cache[data.username][0]:
        return True #print 'authorized user'
    else:
        return False # print 'invalid user'

#if __name__=="__main__":
#      return sign_up(sign_up_object)
#      return log_in(login_object)


