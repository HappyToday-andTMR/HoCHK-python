import turtle as t
t.penup()
t.shape('turtle')
t.bgcolor('cyan')
t.speed(0)
t.showturtle()
def rect(horizonal,vertical,color):
    t.pendown()
    t.color(color)
    t.begin_fill()
    for counter in range(0,2):
        t.forward(horizonal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()
def tri(x,y,a,color):
    t.goto(x,y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for c in range(3):
        t.forward(a)
        t.left(120)
    t.end_fill()
    t.penup()

#feet
t.goto(-80,-150)
rect(40,20,'blue')
t.goto(-30,-150)
rect(50,20,'blue')
#legs
t.goto(-25,-50)
rect(15,100,'red')
t.goto(-58,-50)
rect(15,100,'red')
#body
t.goto(-90,150)
rect(100,200,'green')
#arms
t.goto(-140,70)
rect(50,15,'purple')
t.goto(-140,120)
rect(15,50,'purple')
t.goto(10,70)

rect(50,15,'purple')
t.goto(45,120)
rect(15,50,'purple')
t.goto(45,120)
#hand
t.goto(52,120)
t.begin_fill()
t.color('orange')
t.circle(10)
t.goto(-133,120)
t.circle(10)
t.end_fill()
#neck
t.goto(-50,170)
rect(20,20,'tan')
#head
t.goto(-80,220)
rect(80,50,'red')
#hat
tri(-80,220,80,'dark blue')
#eyes
t.goto(-54,210)
rect(30,10,'white')
t.goto(-50,208)
rect(5,5,'black')
t.goto(-35,208)
rect(5,5,'black')
#mouth
t.goto(-60,185)
rect(40,5,'blue')
#HIde the turltle on the screen
t.hideturtle()
