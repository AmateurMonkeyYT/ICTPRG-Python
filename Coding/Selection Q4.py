username1 = "bob"
password1 = "password1234"

username2 = "fred"
password2 = "happyPass122"

username3 = "lock"
password3 = "passwithlock44"

grantAccess = False

userIn = input("------------------------------------- \nEnter username: ")
passIn = input("Enter password: ")

if (userIn == username1) and (passIn == password1):
    grantAccess = True
elif (userIn == username2) and (passIn == password2):
    grantAccess = True
elif (userIn == username3) and (passIn == password3):
    grantAccess = True

if (grantAccess == True):
    print("Access Granted! \n-------------------------------------")
elif (grantAccess == False):
    print("Access Denied! \n-------------------------------------")