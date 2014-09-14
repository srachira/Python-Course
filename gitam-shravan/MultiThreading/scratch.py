import threading


# creating a thread.
class Worker(threading.Thread):
    def __init__(self,x):
        self.x = x
        threading.Thread.__init__(self)
    def run (self):
        i = 0
        while i < 10:
            print threading.current_thread().name, "[", str(self.x), "]"


def thread_demo():
    for x in xrange(10):
        worker_thread = Worker(x)
        worker_thread.start()


count = 0

def increment():
    global count
    count += 1


# sample race condition, what locks will u you use to make this thread safe?
class Account(object):
    def __init__(self):
        self.lock=threading.RLock()
        self.balance = 0

    def get_balance(self):
        return self.balance


    def set_balance(self, value):
        with self.lock:
            self.balance = value

    def debit(self, value):
        with self.lock:
            balance = self.get_balance()
            time.sleep(5)
            balance -= value
            self.set_balance(balance)


    def credit(self, value):
        with self.lock:
            balance = self.get_balance()
            time.sleep(3)
            balance += value
            self.set_balance(balance)


import urllib2, json, time

#urls = ['http://www.google.com', 'http://www.yahoo.com', 'http://www.stackoverflow.com']
urls = ['http://www.google.com', 'http://www.google.com', 'http://www.google.com']
results = []

start_time = None

def fetch(url):
    response = urllib2.urlopen(url)
    result = response.read()
    print 'Finished fetching {0} url at time {1}'.format(url, time.time() - start_time)


def sequential_fetch():
    for url in urls:
        fetch(url)

def parallel_fetch():
    for url in urls:
        t = threading.Thread(None, target = fetch, args =(url,))
        t.start()

def check_account():
    account_thread=Account()
    t=threading.Thread(None, target=account_thread.set_balance, args=(10000,))
    t.start()
    print account_thread.balance
    t1=threading.Thread(None, target=account_thread.debit, args=(3000,))
    t1.start()
    print account_thread.get_balance()
    t2=threading.Thread(None, target=account_thread.credit, args=(2000,))
    t2.start()
    print account_thread.get_balance()
    t.join()
    t1.join()
    t2.join()
    print account_thread.get_balance()

def parallel_account():
    pass
def main():
    # thread_demo()

    #global start_time
    #start_time = time.time()
    #sequential_fetch()
    #
    #start_time = time.time()
    #parallel_fetch()
    #Sequential For ACCOUNT!

    check_account()
if __name__ == "__main__":
    main()