#24th Jan,2021

# Use Random , Turtle
import random
import turtle as t

# Function -> Get Line Length()
# Parameter list -> Empty
# Get user input to define the line length

def get_line_length(): #alternative getLineLength()

    #get input from use via "Stardard Input (stdin)"
    choice = input('Enter line length（long, medium, short):')
    #dispaly what do wwe get from the user?
    print(choice)
    #check pre-defined string
    if choice == 'long':
        lineLength = 100
    elif choice == 'medium':
        lineLength = 50
    elif choice == 'short':
        lineLength = 25
    #return a string to the caller
    return lineLength

# Function -> Get LIne Width()
# Get user input to define the line Width
def get_line_width(): #alternative getLineLength()

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

# Function *TODO* -> Inside Window()
# Give a bounding box for the movement of the turtle
def inside_window():

    border = 100
    
    left_limit  = (-t.window_width () / 2) + border
    right_limit = ( t.window_width () / 2) - border
    top_limit   = ( t.window_height() / 2) - border
    bottom_limit= (-t.window_height() / 2) + border

    (x,y) = t.pos()

    inside = (left_limit < x < right_limit) and (bottom_limit < y < top_limit)
    
    return inside
    
# Function *TODO* -> Move Turtle()
# Control the randomized movement of the Turtle
def move_turtle(line_length):

    # a collection of color
    pen_color = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    t.pencolor(random.choice(pen_color))
    t.fillcolor(random.choice(pen_color))

    # Stamp the turle on the screen
    t.stamp()

    # control movement
  #  t.right(45)
  #  t.forward(line_length)

    if inside_window():
        angle = random.randint(0, 180)
        t.right(angle)
        t.forward(line_length)
    else:
        t.backward(line_length)

# main program
line_length = get_line_length()
line_width = get_line_width()
t.speed(0)
t.shape('turtle')
t.pensize(line_width)

print(t.window_width())
print(t.window_height())

# An Infinite Loop for the turtle movement
while True:
    move_turtle(line_length)
