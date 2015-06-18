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
    dIndex = 0
    for i in range(len(dVal)):
        if dVal[i] == 'd':
            dIndex = i
    dice = int(dVal[0:dIndex])
    sides = int(dVal[dIndex+1:len(dVal)])
    rollSum = 0
    for r in range(dice):
        rollVal = random.randint(1, sides)
        print 'Roll', r+1, ':', rollVal
        rollSum += rollVal
    print 'Sum: ', rollSum

# Main loop
while(True):
    dVal = raw_input('Input: ')
    if dVal == 'exit':
        sys.exit()
    if dVal == 'help':
        print 'Format: #d# where # is an int, 0 to 20'
    if not validInput(dVal):
        print 'Please input a valid command. (\'help\' for format)'
        continue
    diceRoll(dVal)
