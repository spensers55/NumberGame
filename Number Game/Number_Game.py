# This project will let the user play either side of the game: the guesser or the generator.
# The player is asked which side they want to play at the beginning
import random
import tkinter

counter = 0 # global counter variable

def userPlay(): # NOTE: this function is not being used in the current build
    global counter
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
# end function



def compPlay():
    # this function splits the difference between the current top and bottom bounds, adjusts
    # the top and bottom bounds based on response from checks, and repeats
    global counter
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
#end function


def quitButton(window): # pass in a scene to close
    window.destroy() # close passed in scene

def main(): # this function runs most of the UI Logic of the program
    scene = tkinter.Tk() # create main window
    tkinter.Label(scene, text="Guessing Game Menu: Please Choose").grid(row=0,column=0) # set menu label
    tkinter.Button(scene, text="Play", command=lambda:userPlayUI()).grid(row=1,column=0) # buttons for options
    tkinter.Button(scene, text="Generate", command=lambda:compPlay()).grid(row=2,column=0)
    tkinter.Button(scene, text="Quit", command=lambda:quitButton(scene)).grid(row=3,column=0)
    scene.mainloop() # set to mainloop
#end function

def checkVal(scene, entryBox, target, rlabe, glabe, clabe): # function to check the value of the guess and perform logic
    # rlabe = response label: Tells user too high/low
    # glabe = guess label: tells user what the previous guess was
    # clabe = counter label: tells user how many guesses they've made
    global counter # increment global counter
    counter = counter + 1
    clabe.config(text = "Number of guesses: {0}".format(counter)) # update counter on UI


    guess = int(entryBox.get() or 0) # update guess variable
    glabe.config(text="Previous guess: {0}".format(guess)) # update guess on UI
    entryBox.delete(0, tkinter.END) # clear entry box

    if guess == target: # check guess
        rlabe.config(text="You guessed it!") # if yes, respond and make quit button
        tkinter.Button(scene, text="Quit",command=lambda:quitButton(scene)).grid(row=0,column=1)

    elif guess > target: # if too high, tell user
        rlabe.config(text = "Too High")
        
    else: # if too low, tell user
        rlabe.config(text = "Too Low")
        
#end function

def userPlayUI(): # this function runs the game for the user in the GUI
    UserScene = tkinter.Tk() # create new window
    tkinter.Label(UserScene, text="User Game").grid(row=0,column=0) # title label

    guess = -1 # create guess variable
    global counter # pull global counter
    counter = 0 # reset to 0

    target = random.randint(0,1000000) # computer generates a number

    guessLabel = tkinter.Label(UserScene, text="Previous guess: {0}".format(guess)) # set up guess label
    guessLabel.grid(row=1,column=0) # place on grid

    counterLabel = tkinter.Label(UserScene, text="Number of guesses: {0}".format(counter)) # set up counter label
    counterLabel.grid(row=2,column=0) # place on grid

    entryBox = tkinter.Entry(UserScene, text="Enter Guess:") #set up entry box
    entryBox.grid(row=3,column=0) # place on grid

    responseLabel = tkinter.Label(UserScene, text = "Please Guess") # set up response label
    responseLabel.grid(row=4,column=0) # place on grid
    # vvv bind user input to <Return> (enter key), call check and logic function vvv
    entryBox.bind('<Return>', lambda self:checkVal(UserScene,entryBox,target,responseLabel, guessLabel, counterLabel))
    
#while True:
#    choice = input("Would you like to guess [1] or generate [2]? ([3] to quit): ")
#    if choice == "1":
#        userPlay()
#    elif choice == "2":
#        compPlay()
#    elif choice == "3":
#        break
main() # start program