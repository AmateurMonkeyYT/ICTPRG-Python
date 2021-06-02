loginID = input("username? : ") + ":" + input("password? : ")

with open("logins.txt") as infile:
    loginList = infile.readlines()
    for x in loginList:
        x.strip('\n')
        if loginID == x:
            print("Access Granted!")
            exit()
    print("Access Denied!")
infile.close()