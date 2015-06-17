import random

version = '1.0'

# Intro Statement
print 'Hello, and welcome to Dice Simulator v' + version

def validInput(input):
    return True #pass

def diceRoll(input):
    pass

while(True):
    print 'Please input the value to want to roll.'
    print 'Format: #d# where # is an int, 0 to 20'
    print 'Input: ',
    input = 0 #= user input
    if not validInput(input):
        print 'Invalid input.'
        continue
