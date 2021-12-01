import random
import turtle


def printTest():
    print("Hello world!")


# 060
def drawRect():
    turtle.hideturtle()
    for i in range(0, 4):
        turtle.forward(100)
        turtle.right(90)
    turtle.exitonclick()


# 061
def drawTriangle():
    for i in range(0, 3):
        turtle.forward(100)
        turtle.right(120)
    turtle.exitonclick()


# 062
def drawcircle():
    turtle.circle(100)
    turtle.exitonclick()


# 063
def drawRegColr(color, x, y):
    # turtle.color(color)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(0, 4):
        turtle.forward(100)
        turtle.right(90)
    turtle.end_fill()
    # turtle.exitonclick()


if __name__ == '__main__':
    # printTest()
    # 068
    line = random.randint(10, 50)
    count = random.randint(5, 10)
    angle = random.randint(10, 360)

    for i in range(0, count):
        turtle.right(angle)
        turtle.forward(line)

    turtle.exitonclick()

    # 067
    # for i in range(0, 20):
    #     turtle.right(18)
    #     for i in range(0, 8):
    #         # turtle.pencolor(random.choice(["red", "orange", "blue", "yellow", "green", "pink", "black"]))
    #         # turtle.pencolor(random.choice(["#ff00ff", "#012f08", "#0f0ff0", "#1e1281", "#1f200f", "#040fff", "#00ff00"]))
    #         turtle.forward(50)
    #         turtle.right(45)
    # turtle.exitonclick()

    # 066
    # for i in range(0, 8):
    #     # turtle.pencolor(random.choice(["red", "orange", "blue", "yellow", "green", "pink", "black"]))
    #     turtle.pencolor(random.choice(["#ff00ff", "#012f08", "#0f0ff0", "#1e1281", "#1f200f", "#040fff", "#00ff00"]))
    #     turtle.forward(80)
    #     turtle.right(45)
    #
    # turtle.exitonclick()

    # 065
    # turtle.pendown()
    # turtle.right(90)
    # turtle.forward(100)
    #
    # turtle.penup()
    #
    # turtle.goto(40, 0)
    # turtle.pendown()
    #
    # turtle.left(90)
    # turtle.forward(70)
    #
    # turtle.right(90)
    # turtle.forward(50)
    #
    # turtle.right(90)
    # turtle.forward(70)
    #
    # turtle.left(90)
    # turtle.forward(50)
    #
    # turtle.left(90)
    # turtle.forward(70)
    #
    # turtle.penup()
    #
    # turtle.goto(150, 0)
    # turtle.pendown()
    #
    # turtle.forward(70)
    # turtle.right(90)
    # turtle.forward(50)
    # turtle.right(90)
    # turtle.forward(50)
    #
    # turtle.right(180)
    # turtle.forward(50)
    # turtle.right(90)
    # turtle.forward(50)
    # turtle.right(90)
    # turtle.forward(70)
    #
    # turtle.hideturtle()
    #
    # turtle.exitonclick()

    # 064
    # for i in range(0, 5):
    #     turtle.forward(100)
    #     turtle.right(144)
    # turtle.exitonclick()

    # 063
    # drawRegColr("yellow", 0, 0)
    # drawRegColr("red", 200, 200)
    # drawRegColr("blue", -200, -200)
    # turtle.exitonclick()

    # 062
    # drawcircle()

    # 061
    # drawTriangle()

    # 060
    # drawRect()

    # scr = turtle.Screen()
    # #scr.bgcolor("yellow")
    # turtle.pensize(10)
    # turtle.shape("turtle")
    # turtle.begin_fill()
    # turtle.color("black", "red")
    # for i in range(0,10):
    #     turtle.right(36)
    #     for j in range(0,5):
    #         turtle.forward(100)
    #         turtle.right(72)
    # turtle.exitonclick()
