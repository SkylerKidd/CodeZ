import random

version = '1.0'

# Intro Statement
print 'Hello, and welcome to Dice Simulator v' + version

# Checks if user input was a valid format
def validInput(input):
    return True #pass

# Roll and print result
def diceRoll(input):
    pass

# Main loop
while(True):
    print 'Please input the value to want to roll.'
    print 'Format: #d# where # is an int, 0 to 20'
    print 'Input: ',
    input = 0 #= user input
    if not validInput(input):
        print 'Invalid input.'
        continue
    diceRoll(input)
