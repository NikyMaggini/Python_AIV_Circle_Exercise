import turtle
from circle_exercise import MyCircle


t = turtle.Turtle()

a = MyCircle(15)
b = MyCircle(100)
c = MyCircle(200)


def draw_circle(x, y, circle):
    t.pu()
    t.goto(x, y - circle._radius)
    t.pd()
    t.circle(circle._radius)


draw_circle(-300, 300, a)
draw_circle(50, 30, b)
draw_circle(30, 50, c)