print"Hello!!"
print"Welcome to spychat"
print"Let's get started"
spy_name=raw_input("what is your spy name")
if len(spy_name)>=3:  #block of code
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
        print"Authentication complete. Welcome " + spy_name + " age: " + `spy_age` + " and rating of: " + `spy_rating` + " Proud to have you onboard"





    else:
        print"your age not applicable to be a spy"
else:
    print"Invalid name please re-enter a valid name"