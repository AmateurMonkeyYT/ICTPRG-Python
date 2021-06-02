# Q1

# while True:
#     x = input("please enter a number: ")
#     if x.isdigit():
#         print(x)
#         exit()
#     else:
#         print("not a valid number")



# Q2

# while True:
#     valid = True
#     x = input("please enter an ipv4 address: ")
#     ip = x.split(".")
#     if len(ip) == 4:
#         for i in ip:
#             if (i.isdigit()) and (valid == True):
#                 if (int(i) >= 0) and (int(i) <= 255) and (valid == True):
#                     continue
#                 else:
#                     print("invalid ip address, " + i + " is out of range.")
#                     valid = False
#                     break
#             else:
#                 print("invalid ip address, input is not an ip address.")
#                 valid = False
#                 break
#     else:
#         print("invalid ip address, does not contain 4 values.")
#         valid = False
#     if valid == True:
#         print(x)
#         exit()



# Q3

# while True:
#     upper = False
#     lower = False
#     digit = False
#     symbol = False
#     password = False
#     pw = []
#     x = input("enter a password: ")
#     if len(x) >= 7:
#         for i in x:
#             pw.append(i)
#             if i.isupper():
#                 upper = True
#             elif i.islower():
#                 lower = True
#             elif i.isdigit():
#                 digit = True
#             elif i.isascii() != i.isalnum():
#                 symbol = True
#             else:
#                 continue
#         for n in range(0,len(x)-7):
#             passCheck = ""
#             check = pw[n:n+8]
#             for c in check:
#                 passCheck += c
#             if passCheck == "password":
#                 password = True
#             else:
#                 continue
#     if upper == lower == digit == symbol == True:
#         if password == True:
#             print("invalid password")
#         else:
#             if input("confirm password: ") == x:
#                 print("valid password")
#                 exit()
#             else:
#                 print("passwords do not match")
#     else:
#         print("invalid password")



# Q4

# minWC = input("Enter the minimum word count: ")
# maxWC = input("Enter the maximum word count: ")

# while True:
#     if minWC.isdigit() == maxWC.isdigit() == True:
#         msg = input("Enter your message: ").lower()
#         msgS = msg.split(" ")
#         if int(minWC) <= len(msgS) <= int(maxWC):
#             print(msgS)
#             exit()
#         else:
#             print("Messsage does not meet word count constraints")
#     else:
#         print("Please enter numbers only")



# Q5

# while True:
#     hasDot = False
#     x = input("please enter an email address: ")
#     emS = x.split("@")
#     if len(emS) == 2:
#         if 2 < len(emS[0]) < 32:
#             for i in emS[1]:
#                 if i == ".":
#                     hasDot = True
#                 else:
#                     continue
#         else:
#             print("invalid email address (length)")
#     else:
#         print("invalid email address (does not contain exactly 1 '@')")
#     if hasDot == True:
#         print(x)
#         exit()