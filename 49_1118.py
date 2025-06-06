import turtle

pen = turtle.Turtle()
pen.up()
pen.goto(-200,-200)
pen.down()
pen.color("red")
pen.fillcolor("yellow")
pen.begin_fill()
for i in range(4):
    pen.forward(200)
    pen.left(90)
pen.end_fill()

pen.up()

pen.goto(100,100)

pen.down()

for i in range(3):
    pen.forward(100)
    pen.left(120)

turtle.done()
