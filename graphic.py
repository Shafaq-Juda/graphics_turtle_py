import turtle
import colorsys

t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("black")
t.speed(25)
n=50
h=0
for i in range (320):
    c=colorsys.hsv_to_rgb(h, 1, 0.9)
    h+=1/n
    t.color(c)
    t.left(120)
    t.forward(i)

    for j in range (5):
        t.left(10)
        t.forward(i)
