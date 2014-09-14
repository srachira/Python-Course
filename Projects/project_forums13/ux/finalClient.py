import socket
import datetime
import re

import JSON_Socket
from serialization import *
from cache.cachefile import *


class mySocket:
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        else:
            self.sock = sock

    def connect(self, (host, port)):
        self.sock.connect((host, port))

    def send(self, msg):
        sent = self.sock.send(str(msg))
        if sent == 0:
            print "Runtime error"

    def receive(self):
        return self.sock.recv(10024)

    def close(self):
        self.sock.close()

uname = ""
dict_user = {}
authen_dict = {}
forum_details = {}

def signin():
    global dict_user
    while True:
        username = raw_input("Enter Username : ")
        if len(username) <= 20 and re.match("^[a-zA-Z]{1}[a-zA-Z0-9]*$", username):
            break
        else:
            print "\nInvalid Username: Username should be of less than 20 characters and should contains alphanumerics\n"
    while True:
        password = raw_input("Enter Password : ")
        if len(password) >= 6 and len(password) <= 10 and re.match(
                "^[a-zA-Z]{1}[a-zA-Z0-9]*$", password):
            break
        else:
            print "\nInvalid password: Password should be of 6-10 characters and alphanumeric\n"
    authen_dict['action'] = "login"
    authen_dict['name'] = username
    authen_dict['password'] = password
    return authen_dict
    pass


def serialize_date(input):
    check = '('
    year = ""
    month = ""
    date = ""
    for i in range(len(input)):
        if check == '(':
            if input[i] == ',':
                check = ','
                continue
            if i == 0:
                continue
            year += input[i]
            continue
        if check == ',':
            if input[i] == ',':
                check = ')'
                continue
            month += input[i]
            continue
        if check == ')':
            if input[i] == ')':
                break
            date += input[i]
            continue
    return [int(year), int(month), int(date)]


def signup():
    global dict_user
    while True:
        username = raw_input("Choose your Username : ")
        if len(username) <= 20 and re.match("^[a-zA-Z]{1}[a-zA-Z0-9]*$", username):
            break
        else:
            print "\nInvalid Username: Username should be of less than 20 characters and should contains alphanumerics\n"
    while True:
        password = raw_input("Create a Password : ")
        if len(password) >= 6 and len(password) <= 10 and re.match("^[a-zA-Z]{1}[a-zA-Z0-9]*$", password):
            break
        else:
            print "\nInvalid password: Password should be of 6-10 characters and alphanumeric\n"
    print("Enter DOB:")
    while True:
        year = raw_input("Enter Year:")
        month = raw_input("Enter Month:")
        date = raw_input("Enter Date:")
        DOB = int(year), int(month), int(date)
        year, month, date = serialize_date(str(DOB))
        try:
            datetime.date(year,month,date)
        except Exception as e:
            print e
            continue
        if datetime.date.today() - datetime.date(year, month, date):
            break
        if year>2013:
            print "\nEnter Again,Incorrectly entered\n"
            continue
        else:
            print "\nInvalid Date. Please Enter a Valid Date.\n"
    while True:
        email = raw_input("Your current Email Address : ")
        if len(email) <= 30 and re.match("^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$",email):
            break
        else:
            print "\nInvalid Email. Please Enter a Valid Email Address\n"
    dict_user['action'] = "signup"

    dict_user['name'] = username
    dict_user['password'] = password
    dict_user['DOB'] = DOB
    dict_user['email'] = email
    return dict_user

def exit_connection():
    dict_user={}
    dict_user['action'] = "exit"
    return dict_user

def print_sub_forums(d):
    dict_list = [('Subforums', 'Created by')]
    for i, (k, v) in enumerate(d.items(), 1):
        k = '{0}. {1}'.format(i, k)
        dict_list.append((k, v))
    col_width = max(len(word) for row in dict_list for word in row) + 2 # padding
    for row in dict_list:
        print ''.join(word.ljust(col_width) for word in row)

def display():
    print "The forums listed are :"
    print "\t1. EDUCATION"
    print "\t2. SPORTS"
    print "\t3. ENTERTAINMENT"
    print "\t4. TECHNOLOGY"
    print "\t5. NEWS"
    print "\t6. HEALTH"
    print "\t7. MISCELLANEOUS"

def split_client(dict):
    if dict is None or len(dict) == 0 :
        return None,None
    dict1="#".join(dict.values())
    dict_keys=dict.keys()
    return dict1.split('#'),dict_keys

def split_client_one(dict):
    if dict is None or len(dict) == 0 :
        return None,None
    dict1="#".join(dict.keys())
    dict_keys=dict.keys()
    return dict1.split('#'),dict_keys

def main():
    global dict_user
    global uname
    try:
        client = mySocket()
        host = socket.gethostname()
        port = 8100
        client.connect((host, port))
        while True:
            print ""
            print "Welcome To TEAM 13 Forums"
            print "\t1. Sign in"
            print "\t2. Sign Up for Free"
            print "\t3. View Forums"
            print "\t4. Exit"

            choice = raw_input("Please Select an Option : ")

            if choice == '1':
                input = signin()
                uname = input['name']
                client_json = JSON_Socket.json()
                json_object = client_json.deserializer(input)
                client.send(json_object)
                received = client.receive()
                serialized = serialize_auth(received)
                if serialized == "login successful":
                    print "\n","*********Login Successful*********"
                    print "Welcome, " + uname,"\n"
                    while True:
                        data_forum,f_name = display_user(uname)
                        if data_forum['action'] == "break":
                            break
                        while True:
                            client.send(data_forum)
                            a=client.receive()
                            a=a.split(";")
                            display_forums_from_server=a[0]
                            list_ids=a[1]
                            subforums_Json = JSON_Socket.json()
                            output = subforums_Json.serializer(display_forums_from_server)
                            list_output=convert_string_list_to_list(list_ids)
                            data_send = display_user_selected_forum(f_name,output,uname,list_output)
                            if data_send['action'] == "break":
                                break
                            elif data_send['action'] == "LogOut":
                                exit(0)
                            elif data_send['action'] == "open_sub_forum":
                                while True:
                                    sub_forum = data_send['name']
                                    client.send(str(data_send))
                                    questions = client.receive()
                                    cli_json= JSON_Socket.json()
                                    if questions == None:
                                        continue
                                    for i in range(len(questions)):
                                        if questions[i] == ";":
                                            break
                                    id_of_question = questions[(i+1):]
                                    id_of_question = convert_string_list_to_list(id_of_question)
                                    questions= cli_json.serializer(questions)
                                    question,id_q = split_client_one(questions)
                                    operation = display_questions(question,uname,f_name,sub_forum,id_of_question)
                                    if operation['action'] == 'post_question':
                                        sub_forum=operation['sub_forum']
                                        client.send(str(operation))
                                        rcvd = client.receive()
                                        questions=client_json.serializer(rcvd)
                                        if questions['message'] == "unsuccessful":
                                            continue
                                    if operation['action'] == "continue":
                                        break
                                    if operation['action'] == "view_question":
                                        while True:
                                            question_id = operation['question_id']
                                            client.send(str(operation))
                                            received = client.receive()
                                            questions_about = client_json.serializer(received)
                                            if questions_about['message']:
                                                display_reply(questions_about)
                                            result = display_replies(uname,f_name,sub_forum,question_id)
                                            if result['action'] == "break":
                                                break
                                            client.send(result)
                                            about_reply = client.receive()
                                            print_rep_info = serialize_auth(about_reply)
                                            print print_rep_info
                            elif data_send['action'] == "new_sub_forum":
                                sub_forum=data_send["name"]
                                client.send(str(data_send))
                                success = client.receive()
                                success = client_json.serializer(success)
                                for i in success.values():
                                    print i
                else:
                    print "\n$$$$$Invalid Login Credentials. Please re-check them$$$$$\n"
            elif choice == '2':
                input = signup()
                client_json = JSON_Socket.json()
                client.send(client_json.deserializer(input))
                received = client.receive()
                print received
            elif choice == '3':
                display()
            elif choice == '4':
                input=exit_connection()
                client_json = JSON_Socket.json()
                client.send(client_json.deserializer(input))
                client.close()
                break
            else:
                print "\nPlease Select a Valid Option\n"
    except Exception as e:
        print e,"\n$$$$$Error at line 279$$$$$\n"
    pass

def serialize_auth(input):
    x= convert_from_json_object(input)
    return " ".join(x.values())

def view_forum(forum_name):
    try:
        global forum_details
        forum_details['action'] = "view_forum"
        forum_details['forumname'] = forum_name
        return forum_details,forum_name
    except Exception as e:
        print e,"\n$$$$$Error at 292 line$$$$$\n"


def display_questions(questions,uname,forum_name,sub_forum,id_q):
    while True:
        try:
            print ""
            print "\t1. View Questions"
            print "\t2. Post a Question"
            print "\t3. Back"
            option = raw_input("Enter your Choice")
            if option == "1":
                if questions == None:
                    print "\n$$$$$Empty Sub Forum$$$$$\n"
                    d = {}
                    d['action'] = "continue"
                    return d
                for i in range(len(questions)):
                    print "\t" +str(i+1)+"." +  questions[i]
                option = raw_input("Enter the Question Number you wish to view: ")
                if int(option)<1 or int(option)>len(questions):
                    print "\nEnter a valid Question No.\n"
                else:
                    d = {}
                    d['action'] = "view_question"
                    d['forumname'] = forum_name
                    d['sub_forum'] = sub_forum
                    d['question_id'] = id_q[int(option) - 1]
                    return d
            elif option == "2":
                question_new = raw_input("Enter your Question: ")
                d = {}
                d['action'] = "post_question"
                d['forumname'] = forum_name
                d['sub_forum'] = sub_forum
                d['createdby'] = uname
                d['new_question'] = question_new
                return d
                pass
            elif option == "3":
                d ={}
                d['action'] = "continue"
                return d
            else:
                print "\nPlease Select a Valid Option\n"
        except Exception as e:
            print e,"\nPlease Select a valid Option\n"


def display_replies(uname,forum_name,sub_forum,question_id):
    while True:
        try:
            print ""
            print "\t1. Post a Reply"
            print "\t2. Back"
            option = raw_input("Enter your Choice : ")
            if option == "1":
                reply_new = raw_input("Post your Reply here : ")
                d = {}
                d['action'] = "post_answer"
                d['forumname'] = forum_name
                d['sub_forum'] = sub_forum
                d['new_reply'] = reply_new
                d['createdby'] = uname
                d['question_id'] = question_id
                return d
                pass
            elif option == "2":
                d ={}
                d['action'] = "break"
                return d
                pass
            else:
                print "\nPlease Select a Valid Option\n"
        except Exception as e:
            print e,"\nPlease Select a Valid Option\n"

def display_reply(question_about):
    print question_about
    list1 = question_about.values()
    print list1
    k = 1
    for j in list1:
        for i in j:
            print "\t",str(k)+". ",i[1]
            k = k + 1
    print "\n"
    pass

def display_user(user):
    while True:
        try:
            print ""
            print "\t1. View Forums"
            print "\t2. LogOut"
            choice = raw_input("enter 1 or 2: ")
            if choice == "1":
                display()
                print "\t8. Back"
                while True:
                    option = raw_input("Select the Forum you wish to View " + user + ":" )
                    if option == '1':
                       return view_forum("Education")
                    elif option == '2':
                        return view_forum("Sports")
                    elif option == '3':
                        return view_forum("Entertainment")
                    elif option == '4':
                        return view_forum("Technology")
                    elif option == '5':
                        return view_forum("News")
                    elif option == '6':
                        return view_forum("Health")
                    elif option == '7':
                        return view_forum("Miscellaneous")
                    elif option == "8":
                        break
                    else:
                        print "\nPlease select a Valid option\n"
            elif choice == "2":
                d = {}
                d['action'] = "break"
                return d,user
            else:
                print "\nenter either 1 or 2 only\n"
        except Exception as e:
            print e,"\nEnter a correct Option\n"


def display_user_selected_forum(forum_name,output,uname,list_output):
    while True:
        try:
            print ""
            print "\t1. View Sub-forums"
            print "\t2. Create a Sub-forum"
            print "\t3. Back"
            option = raw_input("Select your option " + uname + ":" )
            j=len(output.keys())
            if option == "1":
                while True:
                    output_dict=convert_from_json_object(str(output))
                    if len(output_dict) == 0:
                        print "\n$$$$$No Threads in selected Forum$$$$$\n"
                        d={}
                        d['action']="continue"
                        return d
                    print_sub_forums(output_dict)
                    option = raw_input("Select a sub-forum: ")
                    opt=int(option)-1
                    sub_id=list_output[opt]
                    out=[]
                    out=output_dict.keys()
                    try:
                        index = out.index(option)
                    except Exception as e:
                        print
                    if int(option)<1 or int(option)>len(out):
                        print "Enter a valid option"
                    else:
                        d = {}
                        d['action'] = "open_sub_forum"
                        d['forumname'] = forum_name
                        d['id'] = sub_id
                        d['name']= out[int(option) - 1]
                        return d
                return
            elif option == "2":
                while True:
                    new_sub_forum = raw_input("Enter the name of the Sub-forum :")
                    if len(new_sub_forum)>30:
                        print "\n$$$$$name exceeds the limit 30,enter again$$$$$\n"
                        continue
                    else:
                        break
                d = {}
                d['action'] = "new_sub_forum"
                d['forumname'] = forum_name
                d['name'] = new_sub_forum
                d['createdby'] = uname
                return d
            elif option == "3":
                d = {}
                d['action'] = "break"
                return d
            else:
                print "\nEnter a Valid Option\n"
        except Exception as e:
            print e,"\nEnter a Valid Option\n"



if __name__ == "__main__":
    main()
