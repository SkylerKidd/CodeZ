# Python 3.4

import random, sys

version = '1.0'

# Intro Statement
print ('Hello, and welcome to Dice Simulator v' + version)
print ('Please input the value to want to roll.')

# Checks if user input was a valid format
def valid_input(in_command):
    # Check format: "[int 1-10]d[int 2-20]"
    # check for proper format length
    if (len(in_command) < 3 or len(in_command) > 5):
        return False #fail
    # check for integer type
    try:
        val1, val2 = in_command.split('d')
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
def diceRoll(in_command):
    roll_sum = 0

    dice, sides = in_command.split('d')
    dice = int(dice)
    sides = int(sides)

    for r in range(dice):
        roll_value = random.randint(1, sides)
        print ('Roll', r+1, ':', roll_value)
        roll_sum += roll_value
    print ('Sum: ', roll_sum)

# Main loop
while(True):
    in_command = input('Input: ')
    if in_command == 'exit':
        sys.exit()
    if in_command == 'help':
        print ('Format: #d# where # is an int, 0 to 20')
    if not valid_input(in_command):
        print ('Please input a valid command. (\'help\' for format)')
        continue
    diceRoll(in_command)
