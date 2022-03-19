import turtle

wn = turtle.Screen()

yuri = turtle.Turtle()

yuri.pencolor("pink")

yuri.pensize(2.5)

turtle.Screen().bgcolor("lightgreen")


for i in range (5):

    l = 20*i+20

    yuri.forward(l)

    yuri.left(90)

    yuri.forward(l)

    yuri.left(90)

    yuri.forward(l)

    yuri.left(90)

    yuri.forward(l)

    yuri.up()

    yuri.forward(10)

    yuri.right(90)

    yuri.forward(10)

    yuri.right(180)

    yuri.down()

wn.mainloop()

