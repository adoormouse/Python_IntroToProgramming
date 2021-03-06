# Lesson 3.3: Use Classes
# Mini-Project: Draw Turtles

# turtle is a library we can use to make simple computer
# graphics. Kunal wants you to try drawing a circles using
# squares. You can also use this space to create other
# kinds of shapes. Experiment and share your results
# on the Discussion Forum!

import turtle
turtle_starting_pos = (10, 110)
offset = 45


# Your code here.
def draw_square():
    # initialize window
    window = turtle.Screen()
    window.bgpic("iliketurtles.gif")
    window.setup(width=400, height=400, startx=0, starty=0)
    window.title("I Like Turtles")


    # initialize Turtle starting position for "Turtle Kid"
    myturtle = turtle.Turtle()
    myturtle.penup()
    myturtle.setx(turtle_starting_pos[0])
    myturtle.sety(turtle_starting_pos[1])

    #draw the shape
    myturtle.pendown()
    myturtle.speed(2)
    myturtle.shape("turtle")

    i = 0
    myturtle.right(offset)
    while i < 4:
        i += 1
        myturtle.forward(100)
        myturtle.right(90)

    window.exitonclick()


draw_square()