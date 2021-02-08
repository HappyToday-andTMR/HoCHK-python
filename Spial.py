import turtle as t
from itertools import cycle

colors = cycle(['red', 'orange', 'yellow', 'green','cyan', 'blue', 'purple','pink','grey','brown' ])
def draw_circle(size, angle, shift):
    t.pencolor(next(colors))
    t.circle(size)
    t.right(angle)
    t.forward(shift)
    draw_circle(size + 1, angle + 1, shift + 0.5)
    
t.bgcolor('black')
t.pensize(2)
t.speed(0)
draw_circle(10, 0, 1)

