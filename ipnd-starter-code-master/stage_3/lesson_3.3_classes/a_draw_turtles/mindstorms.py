# Lesson 3.3: Use Classes
# Mini-Project: Draw Turtles

# turtle is a library we can use to make simple computer
# graphics. Kunal wants you to try drawing a circles using
# squares. You can also use this space to create other
# kinds of shapes. Experiment and share your results
# on the Discussion Forum!

import turtle

offset = 20
# Your code here.
def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    evan = turtle.Turtle()
    evan.speed(10)

    i = 0
    evan.right(offset)
    while i < 4:
        i += 1
        evan.forward(100)
        evan.right(90)

    window.exitonclick()

draw_square()