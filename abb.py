import turtle
f1=turtle.Turtle()
colors=["red","orange","yellow","green","blue","indigo","violet"]

for i in range(150):
    f1.pencolor(colors[i % len(colors)])
    f1.width(i/100+1)
    f1.forward(i)
    f1.left(59)

turtle.done()
