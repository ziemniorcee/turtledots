from turtle import *
from random import choice
from settings import Settings
import string

hex_value = list(string.printable[:16])


def make_circle(t, radius):
    t.begin_fill()
    t.pendown()
    t.circle(radius)
    t.penup()
    t.end_fill()


def color():
    col = "#"
    n = 0
    while n < 6:
        col += choice(hex_value)
        n += 1

    return col


screen = Screen()
s = Settings(screen.window_width(), screen.window_height())

turtle = Turtle(shape="arrow", visible=False)
turtle.penup()

turtle.goto(s.start_x, s.start_y)

turtle.speed(0)

while True:
    turtle.fillcolor(color())
    make_circle(turtle, s.r)

    turtle.forward(s.r * 3)
    x, y = turtle.pos()
    if x > s.x_end:
        if y > s.y_end:
            screen.exitonclick()
        else:
            s.start_y += s.r * 3
            turtle.goto(s.start_x, s.start_y)
