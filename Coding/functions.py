# # Q1

# # START
# def AddTwoNumbers(x, y):
#     return x + y
# # END
# # -------------------------------------
# # DO NOT TOUCH ANY CODE BELOW THIS LINE
# print("Test 1 Passed: " + str(AddTwoNumbers(1, 2) == 3))
# print("Test 2 Passed: " + str(AddTwoNumbers(5, 6) == 11))
# print("Test 3 Passed: " + str(AddTwoNumbers(9, 0) != 10))



# # Q2

# # Write the function between the START and END tags
# # START
# def AddInString(a, b, c):
#     return a + b + c
# # END
# # -------------------------------------
# # DO NOT TOUCH ANY CODE BELOW THIS LINE
# print("Test 1 Passed: " + str(AddInString("Hello, ", "bob", ". How are you today?") == "Hello, bob. How are you today?"))
# print("Test 2 Passed: " + str(AddInString("Woah there ", "frank", ", watch your step!") == "Woah there frank, watch your step!"))
# print("Test 3 Passed: " + str(AddInString("Whats the , ", "meaning", " of all of this?") != "What is the meaning of all of this"))
# print("Test 4 Passed: " + str(AddInString("Happy ", "Lappy", " Tappy") == "Happy Lappy Tappy"))



# # Q3
# # Write the function between the START and END tags
# # START
# # def FibonacciAdder(x):
#     a = 0
#     b = 1
#     c = 0
#     for x in range (0, x+1):
#         a = b
#         b = c
#         c = a + b
#         print(a,b,c)
#     return c - 1
# # END
# # -------------------------------------
# # DO NOT TOUCH ANY CODE BELOW THIS LINE
# print("Test 1 Passed: " + str(FibonacciAdder(2) == 1))
# print("Test 2 Passed: " + str(FibonacciAdder(5) == 7))
# print("Test 3 Passed: " + str(FibonacciAdder(10) == 88))



# # Q4
# # Write the function between the START and END tags
# # START
# def MultiplyElementsInList(list):
#     result = 1
#     for x in list:
#         result *= x
#     return result
# # END
# # -------------------------------------
# # DO NOT TOUCH ANY CODE BELOW THIS LINE
# print("Test 1 Passed: " + str(MultiplyElementsInList([1, 2, 3]) == 6))
# print("Test 2 Passed: " + str(MultiplyElementsInList([0, 2, 3]) == 0))
# print("Test 3 Passed: " + str(MultiplyElementsInList([2, 2, 2]) == 8))
# print("Test 4 Passed: " + str(MultiplyElementsInList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 30414093201713378043612608166064768844377641568960512000000000000))



# Q5

# Write the function between the START and END tags
# START
# def IsPalindrome(x):
#     x = x.replace(" ", "")
#     x = x.lower()
#     if (x == x[::-1]):
#         return True
#     else:
#         return False
# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
# print("Test 1 Passed: " + str(IsPalindrome("GlenElg") == True))
# print("Test 2 Passed: " + str(IsPalindrome("Nurses Run") == True))
# print("Test 3 Passed: " + str(IsPalindrome("Nurses") == False))
# print("Test 4 Passed: " + str(IsPalindrome("frank") == False))



# Q6

# Write the function between the START and END tags
# START
# def SortWordsAlphabetically(x):
#     x = x.lower()
#     word = x.split("-")
#     word.sort()
#     return "-".join(word)
# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
# print("Test 1 Passed: " + str(SortWordsAlphabetically("Bob-does-not-like-frank") == 'bob-does-frank-like-not'))
# print("Test 2 Passed: " + str(SortWordsAlphabetically("why-am-i-doing-this-this-is-terrible") == "am-doing-i-is-terrible-this-this-why"))
# print("Test 3 Passed: " + str(SortWordsAlphabetically("frank-kill-zoe-did") == "did-frank-kill-zoe"))



# Q7

# def PrintBoxByWidth(a):
#     for b in range(0, a):
#         print("x", end='')
#     print("")

#     print("x", end='')
#     for b in range(0, a-2):
#         print(" ", end='')
#     print("x", end='')
#     print("")

#     print("x", end='')
#     for b in range(0, a-2):
#         print("o", end='')
#     print("x", end='')
#     print("")

#     print("x", end='')
#     for b in range(0, a-2):
#         print(" ", end='')
#     print("x", end='')
#     print("")

#     for b in range(0, a):
#         print("x", end='')


# PrintBoxByWidth(60)