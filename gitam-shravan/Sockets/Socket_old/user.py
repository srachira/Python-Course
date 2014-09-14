__author__ = 'SuSh'
import urllib2
import urllib
import datetime
import re

dict_user = {}
authen_dict = {}


def signin():
    global dict_user

    username = raw_input("Username : ")
    password = raw_input("Password : ")

    pass

def signup():
    global dict_user
    while True:
        username = raw_input("Choose your Username : ")
        if len(username) <= 20 and re.match("^[a-zA-Z]{1}[a-zA-Z0-9]*$",username ):
            break
        else:
            print "Invalid Username: Username should be of less than 20 characters and should contains alphanumerics"
    while True:
        password = raw_input("Create a Password : ")
        if len(password) >= 6 and len(password) <= 10 and re.match(
                                "^[a-zA-Z]{1}[a-zA-Z0-9]*$", password) :
            break
        else:
            print "Invalid password: Password should be of 6-10 characters and alphanumeric"
    print("Enter DOB:")
    year=raw_input("Enter Year:")
    month=raw_input("Enter Month:")
    date=raw_input("Enter Date:")
    DOB=int(year),int(month),int(date)
    #while True:
    email = raw_input("Your current e-mail address : ")
        #if len(email)<= 30 and re.match("^\b[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\b",email):
            #break
            #pass
        #else:
            #print "Invalid Email: Enter a valid email address"
    dict_user['username'] = username
    dict_user['password'] = password
    dict_user['DOB'] = DOB
    dict_user['email'] = email
    return dict_user

def display():
    print "The forums listed are :"
    print "\t1. EDUCATION"
    print "\t2. SPORTS"
    print "\t3. ENTERTAINMENT"
    print "\t4. TECHNOLOGY"
    print "\t5. NEWS"
    print "\t6. HEALTH"
    print "\t7. MISCELLANEOUS"
    print "\n"

    option = raw_input("Select the Forum you wish to view : ")

    if option == '1':
        print "\nYou have entered Education Forum"
    elif option == '2':
        print "\nYou have entered Sports Forum"
    elif option == '3':
        print "\nYou have entered Entertainment Forum"
    elif option == '4':
        print "\nYou have entered Technology Forum"
    elif option == '5':
        print "\nYou have entered News Forum"
    elif option == '6':
        print "\nYou have entered Health Forum"
    elif option == '7':
        print "\nYou have entered Miscellaneous Forum"
    else:
        print "\nPlease select a Valid option"

    pass


def main():
    global dict_user
    while 1:
        print "Welcome To TEAM 13 Forum :P"
        print "\t 1. Sign in"
        print "\t 2. Sign Up for Free"
        print "\t 3. View Forums"

        choice = raw_input("Please Select an Option : ")

        #print dict_user

        if choice == '1':
            signin()
        elif choice == '2':
            input= signup()
            request=urllib.request.Request(url='http://localhost:8080/signup',data=input)
            response=urllib.request.urlopen(request)
            print response
        elif choice == '3':
            display()
        else:
            print "\nPlease Select a valid Option"

    pass


if __name__ == "__main__":
    main()

