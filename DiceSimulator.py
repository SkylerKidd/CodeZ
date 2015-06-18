import random, sys

version = '1.0'

# Intro Statement
print 'Hello, and welcome to Dice Simulator v' + version
print 'Please input the value to want to roll.'

# Checks if user input was a valid format
def validInput(dVal):
    # Check for validity of command
    return True #pass

# Roll and print result
def diceRoll(dVal):
    pass

# Main loop
while(True):
    dVal = input('Input: ')
    if dVal == 'exit':
        sys.exit()
    if dVal == 'help':
        print 'Format: #d# where # is an int, 0 to 20'
    if not validInput(dVal):
        print 'Please input a valid command. (\'help\' for format)'
        continue
    diceRoll(dVal)
