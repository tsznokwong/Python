import turtle
a=turtle.Turtle()
a.speed(0)

def square(length) :
    a.circle(length, 360, 4)

for i in range(500):
    square(75)
    a.left(4)
