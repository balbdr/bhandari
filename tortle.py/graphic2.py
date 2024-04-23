import turtle
t= turtle.Turtle()

list1 = [ "yellow","red" ,"blue","green"]
t.up()
t.goto(200,0)
for i in range(1000):
    t.down()
    t.begin_fill()
    t.fillcolor(list1[i])
    t.circle(50)
    t.end_fill()
    t.up()
    t.bk(100)
    
    