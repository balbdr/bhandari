import turtle
t=turtle.Turtle()
list1=["purple","red","orange","blue","green"]
for i in range(300):
    t.color(list1[i%5])
    t.pensize(i/100+1)
    t.forward(i)
    t.left(70)