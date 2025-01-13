import turtle
import random
#Adds random function

t = turtle.Turtle()

t.speed(10)

angles = [0, 60, 120, 180, 240, 300]
#giving angles to choose from
colors = ["black", "green", "purple"]
for i in range (1000):
    t.forward (10)
    t.left (random.choice(angles))
#usage of random
    t.color ( colors[i % 3] )


turtle.exitonclick()