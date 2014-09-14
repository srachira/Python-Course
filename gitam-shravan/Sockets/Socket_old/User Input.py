__author__ = 'SuSh'
user_dict={}
import datetime
def user_signup():
    global user_dict
    user_name=raw_input("Enter User name")
    password=raw_input("Enter Your Password")
    email=raw_input("Enter your email")
    s = raw_input("Enter DOB in the FORMAT YYYY-MM-DD")
    dateofbirth=datetime.date(*map(int, s.split('-')))
    user_dict['username']=user_name
    user_dict['password']=password
    user_dict['email']=email
    user_dict['dateofbirth']=dateofbirth
    print user_dict




