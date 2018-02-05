#import spy detail from details.py
from spy_details import spy_salutation, spy_name, spy_age, spy_rating

#define add_status()with parameters
def add_status(current_status_msg):
    if current_status_msg !=None:
        print "your current status msg is "+ current_status_msg
    else:
        print"you don't have any msg currently"

        #ask if to select old status
        status=raw_input("Do you want to select from old status(Y or N)")

        #if use the old status
        if status.upper()=="Y":
            serial_no=1
            for old_status in STATUS_MSG:
                #``backdash used to str and int concatenate
                print `serial_no`+old_status
                serial_no= serial_no+1
            user_selection=input("Which one do u want to select: ")
            if len(STATUS_MSG)>=user_selection:

                new_status=STATUS_MSG[user_selection-1]
            else:
                print"Invalid selection"

        #if not using old status
        elif status.upper()=="N":
            new_status=raw_input("Enter your status: ")
            if len(new_status)>1:
                STATUS_MSG.append(new_status)
            else:
                print"Please enter at least something"
        else:
            print"invalid entry"
        return new_status



#define a function start_chat
def start_chat(spy_salutation, spy_name, spy_age, spy_rating):

    current_status_msg= None
    show_menu=True
    while show_menu:
        menu_choice=input("what u want to do? \n 1.add a status update.\n0.Exit \n")
        if menu_choice==1:
            updated_status_msg = add_status(current_status_msg)
            print"Your status has been set to "+updated_status_msg

        elif menu_choice==0:
            show_menu = False
            print"Exit successfull"
        else:


            print"invalid choice"

# print command is used to print the output
print"Hello"
print"welcome to the world of spy"
# How to use escape sequences
print'let\'s get started'

#define a list named STATUS_MSG that store multi-data-type and store multiple status
STATUS_MSG=[ 'I am i class','Busy', 'can\'t talk spychat only', 'Sleeping', 'Available']

# Ask the spy whether he wants to continue with the default spy or create a new user
spy_exist=raw_input("Are you an exsting user(Y or N)")
if spy_exist.upper() =="Y":
    # import details from another file named spy_details.py
    print "welcome "+spy_salutation+ spy_name+" age is %d:"%(spy_age)+" rating is %.3f"%(spy_rating)+" proud to be on board"

    # call the start_chat() function
    start_chat(spy_salutation, spy_name, spy_age, spy_rating)
elif spy_exist.upper() =="N":

    # taking name as input from user when not exist already
    spy_name=raw_input("please enter ur name")
    if len(spy_name)>3:

        spy_salutation=raw_input("what i call u(Mr. or Ms.)")
        print "welcome "+ spy_salutation +spy_name +" to the world of possibilities of spy"
        print"Glad to meet u.I would like to know more about u."

        spy_age=input("what is your age ")
        # check the age to be a spy must be not greater than 50 and less than 13
        if 12<spy_age<50:
            print "%s"%(spy_age) + " is valid to be the age of a spy"

            # ask for spy_rating
            spy_rating=input("please enter ur rating")

            # conditions according to spy rating
            if spy_rating >= 5:
                print"Good spy"
            elif 3.5<=spy_rating<5:
                print"average spy"
            elif spy_rating<3.5:
                print"bad spy"



            else:
                print"not a valid rating"

                # Make the spy come online
                spy_is_online = True

            # Authentication completed.show all details of spy
            print"AUTHENTICATION COMPLETE.Welcome" + spy_name + " age is %d: " %(spy_age) + " and rating is %.3f" % (spy_rating) + " Proud to be on board."

            # call the start_chat() function
            start_chat(spy_salutation,spy_name, spy_age, spy_rating)




        # if age is not valid
        else:
            print"not appropriatep age to be a spy"
    # if name is not valid
    else:
        print "invalid name enter a valid name"
        # if input entered is wrong
else:
    print"invalid choice"


