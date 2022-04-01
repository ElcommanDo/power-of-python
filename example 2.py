import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen()
t.speed(0)
s.bgcolor("black")
n = 36
h = 0
for i in range(240):
    c = colorsys.hsv_to_rgb(h, 1, 0.9)
    h += 1 / n
    t.color(c)
    t.circle(i)
    t.left(5)
