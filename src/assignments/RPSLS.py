'''
Created on Feb 22, 2015

@author: aethena
'''
# Rock-paper-scissors-lizard-Spock template
import random

# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "Wrong input.Please choose: rock, Spock, paper, lizard or scissors"

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "Wrong option. Choose an input between 0-4"
    
    

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    # print a blank line to separate consecutive games
    print ""
    
    # print out the message for the player's choice and convert choice to number
    print "Player chooses "+ player_choice
    player_number = name_to_number( player_choice )

    # compute random guess for comp_number using random.randrange() and print out choice
    comp_number = random.randrange(0,5)
    comp_choice = number_to_name( comp_number )
    
    # print out the message for computer's choice
    print "Computer chooses " + comp_choice
    # compute difference of comp_number and player_number modulo five
    result = (comp_number - player_number)%5

    # use if/elif/else to determine winner, print winner message
    if result>0 and result<=2:
        print "Computer wins!"
    elif result>=3 and result<=4:
        print "Player wins!"
    else:
        print "Player and computer tie!"
       
       
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


