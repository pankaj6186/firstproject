# importing details of the spy
from spy_details import spy_name, spy_salutation, spy_age, spy_rating

# print command is used to print the output
print"Hello!!"
print"Welcome to spy_chat"

# How to use escape sequences
print'Let\'s get started'

#define a function start_chat

def start_chat(spy_name, spy_age, spy_rating):

    show_menu=True
    while show_menu:
        #use to enter choice
        menu_choice =input("What do you want to do? \n 1. Add a status update\n 0.Exit\n")

        if (menu_choice == 1):
            status=raw_input("enter status please")
            print "updated status is " + status
        elif menu_choice == 0:
            show_menu = False
        else:
            print"invalid choice"


# Ask the spy whether he wants to continue with the default spy or create a new user
spy_exist = raw_input("Are u an existing user (Y or N)")
if spy_exist.upper() == "Y":
    #import details from another file named spy_details.py
    print "Welcome " + spy_salutation + spy_name +" age :%d" %(spy_age) +" rating of: %.3f" %(spy_rating) +" Proud to have you onboard"
    print"we already have ur details"

    #call the start_chat() function
    start_chat(spy_name, spy_age, spy_rating)

elif spy_exist.upper()=="N":
    print"Need to create a new user profile"

    #taking name as input from user when not exist already
    spy_name=raw_input("what is your spy name")
    #check if the name entered or not
    if len(spy_name)>=3:
        print "Welcome "+spy_name + ", Glad to meet you"

        spy_salutation=raw_input("what should we call you(Mr. or Ms.)")

        spy_name = spy_salutation +" " + spy_name

        print "Alright "+spy_name + ", I'd like to know more about you"

        #ask for age
        spy_age=input("Enter your age")

        #check the age to be a spy must be not greater than 50 and less than 13
        if spy_age>12 and spy_age<50:
            print"you age is fine to be a spy"

            #ask for spy_rating
            spy_rating = input("enter your rating: ")

            #conditions according to spy rating
            if spy_rating >= 5:
                print"Great spy"
            elif spy_rating >= 4.5 and spy_rating < 5:
                print"Good spy"
            elif spy_rating >= 3.5 and spy_rating < 4.5:
                print"average spy"
            else:
                print"Bad spy"

            # Make the spy come online
            spy_is_online = True

            #Authentication completed.show all details of spy
            print"Authentication complete. Welcome " + spy_name +"age :%d" %(spy_age) +" rating of: %.3f" %(spy_rating) +" Proud to have you onboard"

            #call the start_chat() function
            start_chat(spy_name, spy_age, spy_rating)

#if age is not valid
        else:
            print"your age not applicable to be a spy"

    #if name is not valid
    else:
        print"Invalid name please re-enter a valid name"

        #if input entered is wrong
else:
    print"wrong input"