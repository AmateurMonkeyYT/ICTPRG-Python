username = "bob"
password = "password1234"

userIn = input("------------------------------------- \nEnter username: ")
passIn = input("Enter password: ")

if (userIn == username) and (passIn == password):
    print("Access Granted! \n-------------------------------------")
elif (userIn != username) or (passIn != password):
    print("Access Denied! \n-------------------------------------")