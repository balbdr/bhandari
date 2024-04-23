import turtle
import time

# Set up the window
wndw = turtle.Screen()
wndw.bgcolor("black")
wndw.setup(width=600, height=600)
wndw.title("Analog Clock")
wndw.tracer(0)

# Initialize the pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)

# Draw the clock face
def draw_clock(hr, mn, sec, pen):
    pen.up()
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color("green")
    pen.pendown()
    pen.circle(210)

    pen.up()
    pen.goto(0, 0)
    pen.setheading(90)
    for _ in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0, 0)
        pen.rt(30)

    # Define clock hands
    hands = [
        ("white", 80, 12),  # Hour hand
        ("blue", 150, 60),  # Minute hand
        ("red", 110, 60),   # Second hand
    ]

    time_set = (hr, mn, sec)
    for hand in hands:
        time_part = time_set[hands.index(hand)]
        angle = (time_part / hand[2]) * 360
        pen.penup()
        pen.goto(0, 0)
        pen.color(hand[0])
        pen.setheading(90)
        pen.rt(angle)
        pen.pendown()
        pen.fd(hand[1])

# Update the clock every second
while True:
    hr = int(time.strftime("%I"))
    mn = int(time.strftime("%M"))
    sec = int(time.strftime("%S"))
    draw_clock(hr, mn, sec, pen)
    wndw.update()
    time.sleep(1)
    pen.clear()

# Keep the window open
wndw.mainloop()
