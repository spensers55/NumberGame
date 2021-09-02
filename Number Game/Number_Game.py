# This project will let the user play either side of the game: the guesser or the generator.
# The player is asked which side they want to play at the beginning
import random

def userPlay():
    print("Generating a number between 0 and 1,000,000...")
    target = random.randint(0,1000000) # computer generates a number
    guess = -1 # init variables
    counter = 0
    while guess != target: # check user guess against target
        guess = int(input("Enter your guess: ")) # get user input
        counter += 1 # count guesses
        if guess > target: # if too high, tell user
            print("Too High")
        else: # if too low, tell user
            print("Too Low")
    print("You got it in {0} guesses!".format(counter)) # success message

def compPlay():
    # this function splits the difference between the current top and bottom bounds, adjusts
    # the top and bottom bounds based on response from checks, and repeats
    target = int(input("Enter a number between 0 and 1,000,000: ")) # accept input number from user
    while target < 0 or target > 1000000: # validate input
        target = int(input("Enter a valid number"))
    top = 1000000   # moving top bound
    bottom = 0      # moving bottom bound
    adjustment = 0  # amount to move by
    counter = 1     # keep track of guesses
    guess = 500000  # starting guess
    while guess != target:  # while computer hasn't guess the number
        if guess > target:  # if guessed too high
            top = int(top - adjustment) # move top bound down
            print("{0} is too high".format(guess))  # show user the searching
        else:   # if guessed too low
            bottom = int(bottom + adjustment)   # move bottom bound up
            print("{0} is too low".format(guess))   # show user the search
        counter += 1 # count guesses
        adjustment = int(top-bottom)/2  # calculate new adjustment
        guess = int(adjustment + bottom)    # split difference for new guess
    print("The computer got it in {0} guesses!".format(counter)) # success message


while True:
    choice = input("Would you like to guess [1] or generate [2]? ([3] to quit): ")
    if choice == "1":
        userPlay()
    elif choice == "2":
        compPlay()
    elif choice == "3":
        break
