from doctest import debug_script
from pydoc import describe
import sys,time,random
from tkinter.tix import INTEGER
from tracemalloc import start
from unittest import skip

location = 0

typing_speed = 50 #wpm
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print ('')
    
def simpleValidation (userInput,requiredInput,errorMessege):
    while(userInput != requiredInput):
        userInput = input(slow_type(errorMessege))
    return userInput

def directionValidation (direction):
    choices = [
        "north",
        "east",
        "south",
        "west"
    ]
    valid = False
    while (valid == False):
        for i in range(len(choices)):
            if (direction == choices[i]):
                valid = True
        if (valid == True):
            return direction
        else:
            direction = input(print("Please enter a valid direction, north, south, east, or west."))

def integerValidation (userInput):
    valid = False
    while (valid == False):
        if (userInput.isdigit()):
            valid = True
        else:
           userInput = input(slow_type("invalid entry, please enter an intiger"))
    return userInput

def startGame ():
    slow_type("Hello, Welcome to your text based Adventure game.")
    slow_type("Please press enter to begin the game.")
    continueInput = input()
    simpleValidation(continueInput, "", "Please press enter to begin the game.")
    print("\n\n")

    newLocation(0)

def newLocation(location):
    description = [
        "an old rotten shack",
        "a ruin of a castle",
        "a cobble road",
        "a thick dence forrest"
    ]
    slow_type("You find yourself in " + description[location])
    

startGame()
