import random

#variables
mistakes = 0
mystery = None
pattern = ""
pastGuesses = []

# for debugging
infiniteGuesses = False

# chooses a random word from the included dictionary file
def chooseMystery():
    global mystery
    mystery = random.choice(open('dictionary.txt').readlines())
    mystery = mystery[:-1]

# sets up the initial pattern of the word
def makePattern():
    global pattern
    global mystery
    for i in range(len(mystery)):
        pattern += "-"

# method to print the corresponging hangman based on number of mistakes
def printHangman():
    print(" -----")
    if mistakes == 0:
        print("|    |")
        print("|")
        print("|")
        print("|")
        print("|")
    elif mistakes == 1:
        print("|    |")
        print("|    0")
        print("|")
        print("|")
        print("|")

    elif mistakes == 2:
        print("|    |")
        print("|    0")
        print("|    |")
        print("|")
    elif mistakes == 3:
        print("|    |")
        print("|    0")
        print("|   /|")
        print("|")
    elif mistakes == 4:
        print("|    |")
        print("|    0")
        print("|   /|\\")
        print("|")
    elif mistakes == 5:
        print("|    |")
        print("|    0")
        print("|   /|\\")
        print("|   / ")
    elif mistakes == 6:
        print("|    |")
        print("|    0")
        print("|   /|\\")
        print("|   / \\")
    print("|")

# prepares and runs the game
def hangman():
    # choose the mystery word
    chooseMystery()
    # makes the pattern
    makePattern()
    print("This is the hangman game.")
    print("Current pattern is: " + pattern)
    # game is ongoing
    while (mistakes < 6 or infiniteGuesses) and pattern != mystery:
        makeGuess()
        print("")
        print("Past Guesses")
        print(pastGuesses)
        printHangman()
        print("")
        print(pattern)
    if pattern == mystery:
        print("Congratulations, you guessed the word")
    else:
        print("GAME OVER!")
        print("The mystery word was " + mystery)



def makeGuess():
    global mistakes
    global pattern
    global pastGuesses
    # prompt the user to enter their guess
    print("Enter your guess")
    # guess should be case insensitive
    guess = input().lower()
    # checks if the guess is legal
    if not guess.isalpha() or len(guess) != 1 or guess in pastGuesses:
        print("invalid guess, please try again")
    # case if the guess is in the word
    elif guess in mystery:
        pastGuesses.append(guess)
        x = list(mystery)
        y = list(pattern)
        for j in range(len(x)):
            if x[j] == guess:
                y[j] = guess
            pattern = ''.join(y)
    # otherwise mistake
    else:
        pastGuesses.append(guess)
        mistakes += 1
    pastGuesses.sort()