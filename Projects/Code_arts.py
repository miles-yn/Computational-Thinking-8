import turtle
import random

t = turtle.Turtle()

t.color ('purple')
t.speed(10)

angles = [0, 60, 120, 180, 240, 300]
for i in range (1000):
    t.forward (10)
    t.left (random.choice(angles))
    

turtle.exitonclick()