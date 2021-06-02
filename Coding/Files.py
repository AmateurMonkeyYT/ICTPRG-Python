# Q5

# loginID = input("username? : ") + ":" + input("password? : ")

# with open("logins.txt") as infile:
#     if loginID == infile.readline():
#         print("Access Granted!")
#     else:
#         print("Access Denied!")
# infile.close()



# Q4

# outfile = open("factorial.txt", "w")
# n = ""
# factor = 1

# for x in range(1,11):
#     n += str(x) + "x"
#     factor *= int(x)
#     output = (str(x) + " = " + n[:-1] + " -> " + str(factor))
#     print(output)
#     outfile.write(output + "\n")
# outfile.close()



# Q3

# outfile = open("names-formatted.txt", "w")

# with open("names.txt") as infile:
#     nameList = infile.readlines()

# for x in nameList:
#     nameSep = x.title()
#     outfile.write(nameSep)

# outfile.close()
# infile.close()



# Q2

# outfile = open("people.txt", "w")

# while True:
#     name = input("Enter a name: ")

#     if name == "":
#         outfile.close()
#         exit()
#     else:
#         outfile.write(name)
#         outfile.write("\n")