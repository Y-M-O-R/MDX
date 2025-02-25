import turtle

turtle.pensize(3)


# side, length

def userDraw(side, length):
    side = int(side)
    length = int(length)
    turtle.color("black", "grey")
    turtle.begin_fill()
    for i in range(side):
        angle = 360 / side
        turtle.forward(length)
        turtle.left(angle)
    turtle.end_fill()

    keepScreen = int(input("clear screan (1) or continue (2): "))

    if keepScreen == 1:
        turtle.clear()


while True:
    s = input("how many sides: ")
    l = input("how long: ")
    userDraw(s, l)
