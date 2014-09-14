__author__ = 'SuSh'
import threading
class MyQueue():
    def  __init__(self,maxsize):
        self.maxsize = maxsize
        self.list=[]
        self.lock=threading.Lock()

    def Nqueue(self):
        self.NQueue.lock.acquire()
        if len(self.list)  <= self.maxsize:
            self.list.append()
        else:
            self.Nqueue.lock.wait()
        self.Nqueue.lock.release()

    def isempty(self):
        if self.list is None:
            return True

    def Dqueue(self):
        self.NQueue.lock.acquire()
        if len(self.list) > 0:
            self.list.pop()


