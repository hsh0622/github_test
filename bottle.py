import turtle

pen=turtle.Turtle()

pen.shape("turtle")

pen.color("red")

pen.fillcolor("yellow")#채우기 색 지정
pen.begin_fill()#채우기 시작

for i in range(4):
    pen.forward(100)
    pen.left(90)

pen.end_fill()#채우기 끝

turtle.done()
