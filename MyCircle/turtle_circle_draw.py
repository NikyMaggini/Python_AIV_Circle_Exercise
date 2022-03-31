import turtle
from circle_exercise import MyCircle

list = []
b = MyCircle(30)
c = MyCircle(40)
d = MyCircle(50)
e = MyCircle(60)

list.append(c)
list.append(b)
list.append(b)
list.append(b)

t = turtle.Turtle()

for i in range(0, len(list) + 1):
    t.circle(list[i]._radius * i)
