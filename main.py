from spy_details import spy_name, spy_age, spy_rating

print"Hello!!"
print"Welcome to spychat"
print"Let's get started"

def start_chat(spy_name, spy_age, spy_rating):
    show_menu=True
    while show_menu:
        menu_choice =input("What do you want to do? \n 1. Add a status update\n 0.Exit\n")

        if (menu_choice == 1):
            status=raw_input("enter status please")
            print "updated status is " + status
        elif menu_choice == 0:
            show_menu = False
        else:
            print"invalid choice"



spy_exist = raw_input("Are u an existing user (Y or N)")
if spy_exist.upper() == "Y":
    print"we already have ur details"
    start_chat(spy_name, spy_age, spy_rating)
elif spy_exist.upper()=="N":

    spy_name=raw_input("what is your spy name")
    if len(spy_name)>=3:
        print "Welcome "+spy_name + ", Glad to meet you"
        spy_salutation=raw_input("what should we call you(Mr. or Ms.)")
        spy_name = spy_salutation +" " + spy_name
        print "Alright "+spy_name + ", I'd like to know more about you"
        spy_age=input("Enter your age")
        if spy_age>12 and spy_age<50:
            print"you age is fine to be a spy"
            spy_rating = input("enter your rating: ")
            if spy_rating >= 5:
                print"Great spy"
            elif spy_rating >= 4.5 and spy_rating < 5:
                print"Good spy"
            elif spy_rating >= 3.5 and spy_rating < 4.5:
                print"average spy"
            else:
                print"Bad spy"
            spy_is_online = True
            print"Authentication complete. Welcome " + spy_name +"age :%d" %(spy_age) +" rating of: %.3f" %(spy_rating) +" Proud to have you onboard"
            start_chat(spy_name, spy_age, spy_rating)


        else:
            print"your age not applicable to be a spy"
    else:
        print"Invalid name please re-enter a valid name"
else:
    print"wrong input"