grade = int(input("What was your grade: "))

if (grade <= 100) and (grade >= 90):
    print("You will receive a \"High Distinction\"")
elif (grade < 90) and (grade >= 80):
    print("You will receive a \"Distinction\"")
elif (grade < 80) and (grade >= 70):
    print("You will receive a \"Credit\"")
elif (grade < 70) and (grade >= 50):
    print("You will receive a \"Pass\"")
elif (grade >=0) and (grade <50):
    print("You will recieve a \"Fail\"")
elif (grade > 100) or (grade < 0):
    print("Invalid grade")