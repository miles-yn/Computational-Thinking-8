import turtle

t=turtle.Turtle()
t.penup()
t.goto(-100, -100)
t.color("black")
t.pendown()

for i in range(6):
    t.forward(100)
    t.left(60)

turtle.exitonclick()