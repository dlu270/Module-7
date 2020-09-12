# Daniel Lu
# 9/12/20

# This function draws a polygon "flower".

import turtle

def drawPentagon(t, sz):
    for i in range (5):
        t.forward(sz)
        t.left(72)
        
wn = turtle.Screen()

bob = turtle.Turtle()
bob.color("pink")
bob.width(5)

drawPentagon(bob,200)

for i in range (8):
    bob.penup()
    bob.left(40)
    bob.pendown()
    drawPentagon(bob,200)

wn.exitonclick()