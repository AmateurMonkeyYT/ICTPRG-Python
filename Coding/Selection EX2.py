word = input("Enter a word: ").lower()
containsVowel = False

if (word.find("a") >= 1) or (word.find("e") >= 1) or (word.find("i") >= 1) or (word.find("o") >= 1) or (word.find("u") >= 1):
    containsVowel = True

if (containsVowel == True):
    print("There is a vowel in your word")
elif (containsVowel == False):
    print("There are no vowels in your word")