import turtle

wn = turtle.Screen()

t = turtle.Turtle()

t.pencolor("pink")

t.pensize(2.5)

turtle.Screen().bgcolor("lightgreen")


def draw_poly(t, n, sz):
    
    for i in range (n):
        t.forward(sz)
        t.left(360/n)

draw_poly(t, 20, 70)

wn.mainloop()




