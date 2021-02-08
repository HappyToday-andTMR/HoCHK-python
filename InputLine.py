#17th Jan,2021

# Use Random, Turtle
import turtle as t
import random

# Functions

# Function -> Get Line Lenth()
# Get user input to define the line lehgth

def getLineLength(): #alternative getLineLength()

    #get input from use via "Stardard Input (stdin)"
    choice = input('Enter line length（long, medium, short):')
    #dispaly what do wwe get from the user?
    print(choice)
    #check pre-defined string
    if choice == 'long':
        lineLength = 250
    elif choice == 'medium':
        lineLength = 150
    elif choice == 'short':
        lineLength = 50
    #return a string to the caller
    return lineLength

# Function -> Get LIne Width()
# Get user input to define the line Width
def getLineWidth(): #alternative getLineLength()

    #get imput from use via "Stardard input (stdin)"
    choice = input('Enter line width（thick, medium, thin):')
    #dispaly what do wwe get from the user?
    print(choice)
    #check pre-defined string
    if choice == 'thick':
        lineWidth = 20
    elif choice == 'medium':
        lineWidth = 10
    elif choice == 'thin':
        lineWidth = 5
    #return a string to the caller
    return lineWidth


#main program

#setup
lineLength = getLineLength()
lineWidth = getLineWidth()
print('the length will be',lineLength,'and the width will be',lineWidth)
#draw
t.shape('turtle')
t.fillcolor('green')
t.pensize(lineWidth)
t.forward(lineLength)

