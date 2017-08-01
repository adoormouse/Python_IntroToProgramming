import turtle

class Shape:

    def __init__(self, points=1, length=0, offset=0, originx=0, originy=0):
        self.points = points
        self.length = length
        self.origin = (originx, originy)
        self.offset = offset

        if points == 1:
            self.rotation = 0
        else:
            self.rotation = 360/points

        # initialize Turtle starting position
        self.turtle = turtle.Turtle()
        self.turtle.penup()
        self.turtle.setx(self.origin[0])
        self.turtle.sety(self.origin[1])


    def draw(self):
        # Begin drawing
        turtle.pendown()
        turtle.speed(0)

        i = 0
        turtle.right(self.offset)
        while i < self.points:
            i += 1
            turtle.forward(self.length)
            turtle.right(self.rotation)

def triangle(size=100, offset=0):
    """This draws a simple triangle (3-sides)"""
    myshape = Shape(3, size, offset)
    myshape.draw()

def line(size=200, offset=0):
    """Draws a line"""
    myshape = Shape(1, size, offset)
    myshape.draw()

def draw_flower():
    """Uses triangle and line objects to draw a flower, also creates the window which to draw objects in"""
    # initialize window
    window = turtle.Screen()
    window.bgpic("iliketurtles.gif")
    window.setup(width=400, height=400, startx=0, starty=0)
    window.title("I Like Turtles")
    myoffset = 5
    for i in range(0,int(360/myoffset)):
        triangle(100, myoffset)
    for i in range(0,int(360/myoffset)):
        triangle(50, myoffset)

    line(200,90)

    window.exitonclick()

draw_flower()