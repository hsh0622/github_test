import turtle

pen = turtle.Turtle()

pen.color("red")
pen.circle(100)

for i in range(3):
    pen.color("blue")
    pen.forward(200)
    pen.left(120)

for i in range(4):
    pen.color("green")
    pen.forward(200)
    pen.left(90)
    
turtle.done()
