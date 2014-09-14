__author__ = 'Vineeth'

import socket
import time
from json_parser import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('127.0.0.1', 5002))

max_message_length = 1024

def send_message(msg):
        total_sent = 0
        while total_sent < len(msg):
            sent = s.send(msg[total_sent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            total_sent = total_sent + sent

#GET Requests

#retrieving forum1 categories
msg = "GET forum1/category/all"
s.send("MESSAGE_LENGTH " + str(len(msg)))
data = s.recv(1024)
print data
if data == 'Success':
    send_message(msg)
    data = s.recv(1024)
    print data

#retrieving  all forums
msg = "GET forums/all"
s.send("MESSAGE_LENGTH " + str(len(msg)))
data = s.recv(1024)
print data
if data == 'Success':
    send_message(msg)
    data = s.recv(1024)
    print data

#retrieving questions of forum1, category5
msg = "GET forum1/category5/questions/all"
s.send("MESSAGE_LENGTH " + str(len(msg)))
data = s.recv(1024)
print data
if data == 'Success':
    send_message(msg)
    data = s.recv(1024)
    print data

#Error header
msg = "GET forum1/all"
s.send("MESSAGE_LENGTH " + str(len(msg)))
data = s.recv(1024)
print data
if data == 'Success':
    send_message(msg)
    data = s.recv(1024)
    print data


#POST Requests
msg = 'POST {"forumName":"Algorithms"}'
s.send("MESSAGE_LENGTH " + str(len(msg)))
data = s.recv(1024)
print data
if data == 'Success':
    send_message(msg)
    data = s.recv(1024)
    print data

msg = "GET forum2/category3/questions/all"
s.send("MESSAGE_LENGTH " + str(len(msg)))
data = s.recv(1024)
print data
if data == 'Success':
    send_message(msg)
    data = s.recv(1024)
    print data

#Large Data
msg = "a" * 10
s.send("MESSAGE_LENGTH " + str(len(msg)))
data = s.recv(1024)
print data
if data == 'Success':
    send_message(msg)
    data = s.recv(1024)
    print data

s.close()