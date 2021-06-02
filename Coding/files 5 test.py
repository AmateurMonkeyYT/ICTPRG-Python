loginIDs = input("username: ") + ":" + input("password: ")

with open("logins.txt") as IDfile:
    IDlist = IDfile.readlines()
    for x in IDlist:
        if (loginIDs + "\n") == x:
            print("Access Granted!")
            exit()
    print("Access Denied.... Go away!")
IDfile.close