#importing Turtle
import turtle
t = turtle.Turtle()
def setpen(x, y):
    #  pen up
    t.penup()
    #  let's move the brush to (x, y)
    t.goto(x, y)
    #  put pen to paper
    t.pendown()
    t.setheading(0)

def circle(x, y, r, color):
    #  to make sure we draw a circle that is round enough, we set the edges of the circle a little bit more
    n = 36
    angle = 360 / n
    pi = 3.1415926
    #  the perimeter
    c = 2 * pi * r
    #  the length of each side
    l = c / n
    #  the starting position
    start_x = x - l / 2
    start_y = y + r
    # To move the brush
    setpen(start_x, start_y)
    # select the brush color
    t.pencolor(color)
    #  select background color
    t.fillcolor(color)
    #  fill
    t.begin_fill()
    for i in range(n):
        t.forward(l)
        t.right(angle)
    t.end_fill()

def five_star(l):
    setpen(0, 0)
    t.setheading(162)
    t.forward(150)
    t.setheading(0)
    t.fillcolor('WhiteSmoke')
    t.begin_fill()
    t.hideturtle()
    t.penup()
    for i in range(5):
        t.forward(l)
        t.right(144)
    t.end_fill()

def sheild():
    circle(0, 0, 300, 'red')
    circle(0, 0, 250, 'white')
    circle(0, 0, 200, 'red')
    circle(0, 0, 150, 'blue')
    five_star(284)

if __name__ == '__main__':
    sheild()
    #  end turtle
    turtle.done()
