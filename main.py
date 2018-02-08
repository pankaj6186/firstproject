# import spy detail from details.py
from spy_details import spy

# import steganography class from python library
from steganography.steganography import Steganography

# from datetime library import date-time
from datetime import datetime

# define add_status() function with parameters
def add_status(current_status_msg):
    if current_status_msg != None:
        print "your current status msg is" + current_status_msg
    else:
        print"you don't have any status currently"

        # ask if to select old status
    status=raw_input("Do you want to select from old status? Y or N: ")
    if len(status) >= 1:

            # if use the old status
        if status.upper() == "Y":
            serial_no=1
            for old_status in STATUS_MSG:
                # %d %s used to str and int concatenate
                print"%d . %s" % (serial_no, old_status)
                serial_no = serial_no + 1

            user_selection=input("Which one do u want to select: ")
            if len(STATUS_MSG) >= user_selection:

                new_status=STATUS_MSG[user_selection-1]
            else:
                print"Invalid selection"
            return new_status




            #if not using old status
        elif status.upper()=="N":
            new_status=raw_input("Enter your status: ")
            if len(new_status)>1:
                STATUS_MSG.append(new_status)
        else:
            print"invalid entry"
        return new_status

    else:
        set_status= 'No status'
        return set_status


# define add_friend() function to adda friend
def add_friend():
    # define a dictionary that also contains a list
    new_friend = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0,
        'chats':[]
    }

    new_friend['name']=raw_input("what is the name of friend")
    new_friend['salutation']=raw_input("what should we call ur friend? Mr. or Ms. ")
    new_friend['name']=new_friend['salutation']+" "+new_friend['name']
    new_friend['age']=input("friend age")
    new_friend['rating']=input("friend rating")
    if len(new_friend['name']) >=3 and 50>=new_friend['age']>= 12 and new_friend['rating'] >=spy['rating']:
        # append() function of list friends used to append details in dictionary new_friend
        friends.append(new_friend)

    else:
        print"Friends cannot be added"
    return len(friends)

# define select_a_friend() function to select a friend from choices given
def select_a_friend():
    serial_no=1
    for frnd in friends:
        print str(serial_no)+" "+frnd['name']
        serial_no=serial_no+1
    user_selected_friend=input("Select ur friend: ")
    user_index = int(user_selected_friend)-1
    return user_index

# define send_message() function to send secret message to someone
def send_message():
    user_friend_index = select_a_friend()
    original_image = raw_input("What is the name of your image? ")
    text = raw_input("What is ur secret message? ")
    output_path = 'output.jpg'
    # use of steganography library function encode to encode a message in image
    Steganography.encode(original_image, output_path, text)
    new_chat = {
        "message": text,
        "time": datetime.now(),
        "sent_by_me": True
    }
    # append new_chat to friends list
    friends[user_friend_index]['chats'].append(new_chat)
    print "Your secret message is ready!!!"


# define read_message() function to read the encrypted message
def read_message():
    sender= select_a_friend()
    output_path = raw_input("What is the name of ur encrypted file? ")
    # use decode() function of steganography library to decode the encoded message
    Decrypted_text = Steganography.decode(output_path)

    new_chat = {
        "message": Decrypted_text,
        "time": datetime.now(),
        "sent_by_me": False
    }
    print "Your secret message is:" + Decrypted_text

    friends[sender]['chats'].append(new_chat)
    print "Your secret message has been saved!"


            #define a function start_chat
def start_chat(spy_name, spy_age, spy_rating):

    current_status_msg= None
    show_menu = True
    while show_menu:
        menu_choice=input("what u want to do? \n 1.add a status update.\n 2. Add a new friend.\n 3.Send a message.\n 4.Read a message.\n 5. Read chat history\n 0.Exit \n")
        if menu_choice == 1:
            current_status_msg = add_status(current_status_msg)
            if len(current_status_msg) >= 1:
               if current_status_msg == 'No status':
                   print"You didn't select the status correctly"
               else:
                 print"Your status has been set to " + current_status_msg
            else:
                print"You didn't select the status correctly"

        elif menu_choice==2:
           no_of_friends =add_friend()
           print"you have "+str(no_of_friends) +" no of friends"

        elif menu_choice ==3:
            send_message()
        elif menu_choice ==4:
            read_message()



        elif menu_choice == 0:
            show_menu = False

    else:
        print"invalid choice"




#define a list named STATUS_MSG that store multi-data-type and store multiple status
STATUS_MSG=[ 'I am i class','Busy', 'can\'t talk spychat only', 'Sleeping', 'Available']

friends = [{'name':'Amit','age':28,'rating':5.0,'chats':[]}, {'name':'vinay','age':28,'rating':5.6,'chats':[]}]


# print command is used to print the output
print"Hello"
print"welcome to the world of spy"
# How to use escape sequences
print'let\'s get started'

# Ask the spy whether he wants to continue with the default spy or create a new user
spy_exist=raw_input("Are you an exsting user(Y or N)")
if spy_exist.upper() == "Y":



    # import details from another file named spy_details.py
    print "welcome "+ spy['name']+" age is %d:"%(spy['age'])+" rating is %.3f"%(spy['rating'])+" proud to be on board"

    # call the start_chat() function
    start_chat(spy['name'], spy['age'], spy['rating'])

elif spy_exist.upper() == "N":

    spy = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0
    }

    # taking name as input from user when not exist already
    spy['name']=raw_input("What is ur name")
    if len(spy['name'])>3:
        print "welcome " + spy['name'] + " to the world of possibilities of spy"
        print"Glad to meet u.I would like to know more about u."

       



        spy['age']=input("what is your age ")
        # check the age to be a spy must be not greater than 50 and less than 13
        if 12<spy['age']<50:
            print "%s"%( spy['age']) + " is valid to be the age of a spy"

            # ask for spy['rating']
            spy['rating']=input("please enter ur rating")

            # conditions according to spy rating
            if spy['rating'] >= 5:
                print"Good spy"
            elif 3.5<=spy['rating']<5:
                print"average spy"
            elif spy['rating']<3.5:
                print"bad spy"



            else:
                print"not a valid rating"

                # Make the spy come online
                spy_is_online = True

            # Authentication completed.show all details of spy
            print"AUTHENTICATION COMPLETE.Welcome" + spy['name'] + " age is %d: " %(spy['age']) + " and rating is %.3f" % (spy['rating']) + " Proud to be on board."

            # call the start_chat() function
            start_chat(spy['name'], spy['age'], spy['rating'])




        # if age is not valid
        else:
            print"not appropriatep age to be a spy"
    # if name is not valid
    else:
        print "invalid name enter a valid name"
        # if input entered is wrong
else:
    print"invalid choice"


