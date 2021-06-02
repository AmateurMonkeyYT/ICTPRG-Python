import random

guessLog = []
i = random.randint(0,25)

print("Hey there! Lets play a little guessing game.")

while True:

    guess = int(input("Guess the number between 0 and 25 \n"))
    guessLog.append(guess)

    # Correct Guess
    if (guess == i):
        print("Damn. You win! \nThe number was indeed", i)
        print("You guessed in", len(guessLog), "guesses\nYour guess log:")
        print(guessLog)
        exit()
    
    # Guess is too high
    elif (guess > i):
        print("Nope, its less than that")
        print("You have", 7 - len(guessLog), "guesses left")
    
    # Guess is too low
    elif (guess < i):
        print("Nope, its greater than that")
        print("You have", 7 - len(guessLog), "guesses left")
    
    # Lose condition
    if (len(guessLog) == 7):
        print("AHAHA YOU LOSE!")
        print("The number was", i, "you fool.")
        print(guessLog)
        exit()