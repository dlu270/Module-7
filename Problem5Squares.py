# Daniel Lu
# 9/12/20

# This function draws a square with several other squares inside of it.

import turtle

def drawSquare(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)
        
wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")

drawSquare(alex,250)

alex.penup()
alex.forward(225)
alex.left(90)
alex.forward(25)
alex.pendown()
drawSquare(alex,200)

alex.penup()
alex.forward(175)
alex.left(90)
alex.forward(25)
alex.pendown()
drawSquare(alex,150)

alex.penup()
alex.forward(125)
alex.left(90)
alex.forward(25)
alex.pendown()
drawSquare(alex,100)

alex.penup()
alex.forward(75)
alex.left(90)
alex.forward(25)
alex.pendown()
drawSquare(alex,50)

wn.exitonclick()