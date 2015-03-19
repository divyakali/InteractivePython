# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

#initialize globals
secret_number = 0
guesses =0
# helper function to start and restart the game
def new_game():
    range100()
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number
    global guesses
    secret_number = random.randrange(0,100)
    guesses = math.ceil(math.log((100+1),2))

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number 
    global guesses
    secret_number = random.randrange(0,1000)
    guesses = math.ceil(math.log((1000+1),2))
    
def input_guess(guess):
    # main game logic goes here	
    print "Guess was " + guess
    guessed_number = int(guess)
    print secret_number
    global guesses
    if guesses > 0:
        if guessed_number<secret_number:
            print "Lower"
            guesses = guesses - 1
        elif guessed_number == secret_number:
            print "Correct"
            guesses = 0
        else:
            print "Higher"
            guesses = guesses - 1
    if guesses==0:
        print "Sorry, you ran out of guesses!"    
            
# create frame
frame = simplegui.create_frame("Guess Number",500,500)

# register event handlers for control elements and start frame
frame.add_input("Guess a number",input_guess,200)
frame.add_button("Range: 0-100",range100,100)
frame.add_button("Range: 0-1000",range1000,100)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
