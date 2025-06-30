import turtle

screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Turtle()
pen.speed(0)
pen.width(1)
pen.hideturtle()

colors = ["red","yellow","blue"]

for i in range(200):
    pen.pencolor(colors[i % 3])
    pen.forward(i * 2)
    pen.left(119)

screen.exitonclick()
