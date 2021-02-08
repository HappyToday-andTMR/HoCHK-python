
import turtle as t
from random import randint, random
t.speed(0)
def drawStar(size,points,x,y,color):
    t.goto(x,y)
    t.pendown()
    angle=180-(180/points)
    t.color(color)  #define the color of the star
    t.begin_fill()  #start filling the star
    for i in range(points):    #repeat 5 times
        t.forward(size)    #draw line
        t.right(angle)    #turn angle
    t.end_fill()    #end filling the star
    t.penup()
t.Screen().bgcolor('black')
#Draw the stars over the skys
for i in range(2021):
    #define parmeters for the stars
    #size
    ranSize = randint(10,50)
    #points
    ranPts = randint(2,5)*2+1
    #x,y
    ranX = randint(-600,600)
    ranY = randint(-300,300)
    #color
    ranColor = (random(), random(), random())
    #Draw star
    drawStar(ranSize, ranPts, ranX, ranY, ranColor)

    
