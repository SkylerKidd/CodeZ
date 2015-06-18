import random, sys

version = '1.0'

# Intro Statement
print('Hello, and welcome to Dice Simulator v' + version)
print('Please input the value to want to roll.')

# Checks if user input was a valid format
def validInput(dVal):
    # Check format: "[int 1-10]d[int 2-20]"
    # check for proper format length
    if (len(dVal) < 3 or len(dVal) > 5):
        return False #fail
    # check for integer type
    try:
        val1, val2 = dVal.split('d')
    except ValueError:
        return False #fail
    try:
        val1 = int(val1)
        val2 = int(val2)
    except ValueError:
        return False #fail
    # check int 1 is in range
    if not (val1 >= 1 and val1 <= 10):
        return False #fail
    # check int 2 is in range
    if not (val2 >= 2 and val2 <= 20):
        return False #fail
    # all conditions met
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
        print('Format: #d# where # is an int, 0 to 20')
    if not validInput(dVal):
        print('Please input a valid command. (\'help\' for format)')
        continue
    diceRoll(dVal)
