__author__ = 'Vineeth'

import socket
from json_parser import *


class ForumServer(object):
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 5002
        self.file_fd = open("forum_data.txt", "r+")
        self.forum_details = convert_to_json_object(self.file_fd.read())

    def create_socket(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            return s
        except socket.error:
            print "Error occured while creating socket"

    def bind(self, sock_obj):
        try:
            sock_obj.bind((self.host, self.port))
            return True
        except socket.error:
            print "Error occured while binding the socket"

    def listen(self, sock_obj, backlog):
        try:
            sock_obj.listen(backlog)
            return True
        except socket.error:
            print "Error occured while listening to socket"

    def get_patterns(self, request_string):
        index, end_index, temp, patterns = 0, len(request_string), '', []
        while index < end_index:
            if request_string[index] == ' ':
                index += 1
                continue
            if request_string[index] != '/':
                temp += request_string[index]
            else:
                patterns.append(temp)
                temp = ''
            index += 1
        if temp:
            patterns.append(temp)
        return patterns

    def return_type_of_request(self, request_string):
        if "GET " in request_string:
            request_string = request_string.replace("GET ", "")
            request_patterns = self.get_patterns(request_string)
            length_of_patterns = len(request_patterns)
            if length_of_patterns == 2:
                return "GET-forums", request_patterns
            elif length_of_patterns == 3:
                return "GET-categories", request_patterns
            elif length_of_patterns == 4:
                return "GET-questions", request_patterns
            else:
                return None, request_patterns
        elif "POST " in request_string:
            request_string = request_string.replace("POST", "")
            json_info = convert_to_json_object(request_string)
            no_of_fields_of_json = len(json_info)
            if no_of_fields_of_json == 1:
                return "ADD-forums", json_info
            elif no_of_fields_of_json == 2:
                return "ADD-categories", json_info
            elif no_of_fields_of_json == 3:
                return "ADD-questions", json_info
            else:
                return None, json_info
        elif "UPDATE " in request_string:
            request_string = request_string.replace("UPDATE", "")
            json_info = convert_to_json_object(request_string)
            no_of_fields_of_json = len(json_info)
            if no_of_fields_of_json == 2:
                return "UPDATE-forums", json_info
            elif no_of_fields_of_json == 3:
                return "UPDATE-categories", json_info
            else:
                return None, json_info
        elif "DELETE " in request_string:
            request_string = request_string.replace("DELETE", "")
            json_info = convert_to_json_object(request_string)
            no_of_fields_of_json = len(json_info)
            if no_of_fields_of_json == 1:
                return "DELETE-forums", json_info
            elif no_of_fields_of_json == 2:
                return "DELETE-categories", json_info
            else:
                return None, json_info
        else:
            return None, None

    def call_appropriate_func(self, type_of_request, extra_args):
        data = ''
        if type_of_request is None:
            data = 'Your Response Header is not accepted'
        elif type_of_request == 'GET-forums':
            forum_name = extra_args[0]
            data = self.retrieve_forums(forum_name)
        elif type_of_request == 'GET-categories':
            forum_name = extra_args[0]
            data = self.retrieve_categories(forum_name)
        elif type_of_request == 'GET-questions':
            forum_name, category_name = extra_args[0], extra_args[1]
            data = self.retrieve_questions(forum_name, category_name)
        elif type_of_request == 'ADD-forums':
            data = self.add_forums(extra_args)
        elif type_of_request == 'ADD-categories':
            data = self.add_categories_to_forums(extra_args)
        elif type_of_request == 'ADD-questions':
            data = self.add_questions_to_categories_in_forums(extra_args)
        elif type_of_request == 'UPDATE-forums':
            data = self.update_forum_name(extra_args)
        elif type_of_request == 'UPDATE-categories':
            data = self.update_category_name_of_forum(extra_args)
        elif type_of_request == 'DELETE-forums':
            data = self.delete_forum(extra_args)
        elif type_of_request == 'DELETE-categories':
            data = self.delete_category_in_forum(extra_args)
        return data

    def retrieve_forums(self, forum_name):
        if 'forums' == forum_name:
            return_list = []
            forum_list = self.forum_details.keys()
            for forum_name in forum_list:
                return_list.append(forum_name)
            return '{"forums": ' + str(return_list) + '}'
        else:
            return '{"Error": "You have entered invalid header format"}'

    def retrieve_categories(self, forum_name):
        if forum_name in self.forum_details.keys():
            return_list = []
            forum_categories = self.forum_details[forum_name]
            forum_categories_list = forum_categories.keys()
            for category_name in forum_categories_list:
                return_list.append(category_name)
            return '{"forumName": "' + forum_name + '"\n' + '"categories": ' + str(return_list) + '}'
        else:
            return '{"Error" : "Invalid Forum Name Given"}'

    def retrieve_questions(self, forum_name, category_name):
        forum_list = self.forum_details.keys()
        if forum_name in forum_list:
            if category_name in self.forum_details[forum_name].keys():
                return_list = []
                questions_list = self.forum_details[forum_name][category_name]
                for question in questions_list:
                    if isinstance(question, list):
                        return_list.append(question[1])
                return '{"forumName": ' + forum_name + '\n' + '"categories": ' + category_name + '\n' + '"questions": '\
                       + str(return_list) + "}"
            else:
                return '{"Error": "Invalid Category Name Given"}'
        else:
            return '{"Error": "Invalid Forum Name Given"}'

    def add_forums(self, json_data):
        if 'forumName' in json_data:
            forum_name = json_data['forumName']
            if forum_name not in self.forum_details.keys():
                self.forum_details[forum_name] = {}
                self.write_file()
                return '{"Success": "Successfully Added Forum"}'
            else:
                return '{"Error": "Forum Name already Exists"}'
        else:
            return '{"Error": "Invalid JSON data given"}'

    def add_categories_to_forums(self, json_data):
        if 'forumName' and 'categoryName' in json_data:
            forum_name, category_name = json_data['forumName'], json_data['categoryName']
            if forum_name in self.forum_details.keys():
                if category_name not in self.forum_details[forum_name].keys():
                    self.forum_details[forum_name][category_name] = [0.0]
                    self.write_file()
                    return '{"Success": "Successfully added category"}'
                else:
                    return '{"Error": "Category Name in ' + forum_name + ' already Exists"}'
            else:
                return '{"Error": "Given Invalid forum name to insert category"}'
        else:
            return '{"Error": "Invalid JSON data given"}'

    def add_questions_to_categories_in_forums(self, json_data):
        if 'forumName' and 'categoryName' and 'questions' in json_data:
            forum_name, category_name, question_list = json_data['forumName'], json_data['categoryName'], \
                                                       json_data['questions']
            if forum_name in self.forum_details.keys():
                if category_name in self.forum_details[forum_name].keys() and isinstance(question_list, list):
                    question_counter = self.forum_details[forum_name][category_name][0]
                    for question in question_list:
                        question_counter += 1
                        self.forum_details[forum_name][category_name].append([question_counter, question])
                    self.forum_details[forum_name][category_name][0] = question_counter
                    self.write_file()
                    return '{"Success": "Successfully added questions"}'
                else:
                    return '{"Error": "Given Invalid Character_name to insert Question or invalid Question data given"}'
            else:
                return '{"Error": "Given Invalid forum Name to insert Question"}'
        else:
            return '{"Error": "Invalid JSON data given"}'

    def update_forum_name(self, json_data):
        if "forumName" and "newForumName" in json_data:
            forum_name, new_forum_name = json_data['forumName'], json_data['newForumName']
            if forum_name in self.forum_details.keys():
                forum_data = self.forum_details[forum_name]
                del self.forum_details[forum_name]
                self.forum_details[new_forum_name] = forum_data
                self.write_file()
                return '{"Success": "Successfully Updated Forum Name"}'
            else:
                return '{"Error": "Given Invalid Forum name to Update"}'
        else:
            return '{"Error":"Invalid Json data given"}'

    def update_category_name_of_forum(self, json_data):
        if "forumName" and "categoryName" and "newCategoryName" in json_data:
            forum_name, category_name, new_category_name = json_data['forumName'], json_data['categoryName'], \
                                                           json_data['newCategoryName']
            if forum_name in self.forum_details.keys():
                if category_name in self.forum_details[forum_name].keys():
                    category_data = self.forum_details[forum_name][category_name]
                    del self.forum_details[forum_name][category_name]
                    self.forum_details[forum_name][new_category_name] = category_data
                    self.write_file()
                    return '{"Success": "Successfully updated category name"}'
                else:
                    return '{"Error": "Given invalid category name to update"}'
            else:
                return '{"Error": "Given Invalid forum name for the category to update"}'
        else:
            return '{"Error": "Invalid JSON data given"}'

    def delete_forum(self, json_data):
        if "forumName" in json_data:
            forum_name = json_data["forumName"]
            if forum_name in self.forum_details.keys():
                del self.forum_details[forum_name]
                self.write_file()
                return '{"Success": "Successfully deleted the forum"}'
            else:
                return '{"Error": "Given Invalid Forum Name to delete"}'
        else:
            return '{"Error": "Invalid JSON data given"}'

    def delete_category_in_forum(self, json_data):
        if "forumName" and "categoryName" in json_data:
            forum_name, category_name = json_data["forumName"], json_data["categoryName"]
            if forum_name in self.forum_details.keys():
                if category_name in self.forum_details[forum_name].keys():
                    del self.forum_details[forum_name][category_name]
                    self.write_file()
                    return '{"Success": "Successfully deleted category name in given forum"}'
                else:
                    return '{"Error": "Given invalid category name to delete"}'
            else:
                return '{"Error": "Given invalid forum name for the category to delete"}'
        else:
            return '{"Error": "Invalid JSON data given"}'


    def write_file(self):
        self.file_fd.seek(0)
        self.file_fd.truncate()
        self.file_fd.write(str(self.forum_details))

    def close_file(self):
        self.file_fd.close()

    def get_message_length(self, data):
        data = data.replace("MESSAGE_LENGTH", "")
        data = data.replace(" ", "")
        if data.isdigit():
            return int(data)
        return None

if __name__ == '__main__':
    forum_obj = ForumServer()
    sock_obj = forum_obj.create_socket()
    forum_obj.bind(sock_obj)
    forum_obj.listen(sock_obj, 5)
    conn, address = sock_obj.accept()
    message_length = None
    try:
        while True:
            message, message_length = '', None
            if message_length is None:
                length_data = conn.recv(1024)
                print length_data
                if "MESSAGE_LENGTH" in length_data:
                    message_length = forum_obj.get_message_length(length_data)
                    if not isinstance(message_length, int):
                        conn.send('{"Error": "Given Invalid message length"}')
                        continue
                    conn.send("Success")
                else:
                    conn.send('{"Error":"Didnt pass the Message Length"}')
                    continue
            if message_length:
                while len(message) < message_length:
                    chunk = conn.recv(message_length-len(message))
                    if chunk == '':
                        raise RuntimeError("socket connection broken")
                    message = message + chunk
                if message:
                    print message
                    type_of_request, patterns = forum_obj.return_type_of_request(message)
                    if type_of_request is None:
                        conn.send('{"Error":"Invalid header"}')
                        continue
                    data = forum_obj.call_appropriate_func(type_of_request, patterns)
                    conn.send(data)
        conn.close()
        sock_obj.close()
    except socket.error:
        print "Exception encountered"
        sock_obj.close()
        sock_obj.close()
