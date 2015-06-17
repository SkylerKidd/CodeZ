import random

version = '1.0'

# Intro Statement
print 'Hello, and welcome to Dice Simulator v' + version

# Checks if user input was a valid format
def validInput(dVal):
    return True #pass

# Roll and print result
def diceRoll(dVal):
    pass

# Checks if user wants to play again
def playAgain():


# Main loop
while(True):
    print 'Please input the value to want to roll.'
    print 'Format: #d# where # is an int, 0 to 20'
    dVal = input('Input: ')
    if not validInput(dVal):
        print 'Invalid input.'
        continue
    diceRoll(dVal)
    playAgain()
