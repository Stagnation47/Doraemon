import turtle
from turtle import *


def flyTo(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def drawEye():
    turtle.tracer(True)
    a = 2.5
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a -= 0.05
        else:
            a += 0.05
        turtle.left(3)
        turtle.fd(a)
    turtle.tracer(True)



def beard():
    positions = [(-37, 135), (-37, 125), (-37, 115), (37, 135), (37, 125), (37, 115)]
    angles = [165, 180, 193, 15, 0, -13]

    for (x, y), angle in zip(positions, angles):
        flyTo(x, y)
        turtle.seth(angle)
        turtle.fd(60)





def drawRedScarf():
    turtle.fillcolor("pink")
    turtle.begin_fill()
    turtle.seth(0)
    turtle.fd(200)
    turtle.circle(-5, 90)
    turtle.fd(10)
    turtle.circle(-5, 90)
    turtle.fd(207)
    turtle.circle(-5, 90)
    turtle.fd(10)
    turtle.circle(-5, 90)
    turtle.end_fill()


def drawMouse():
    flyTo(5, 148)
    turtle.seth(270)
    turtle.fd(100)
    turtle.seth(0)
    turtle.circle(120, 50)
    turtle.seth(230)
    turtle.circle(-120, 100)


def drawRedNose():
    flyTo(-10, 158)
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()


def drawBlackdrawEye():
    turtle.seth(0)
    flyTo(-25, 195)
    turtle.fillcolor("#000000")
    turtle.begin_fill()
    turtle.circle(13)
    turtle.end_fill()
    turtle.pensize(6)
    flyTo(20, 205)
    turtle.seth(75)
    turtle.circle(-10, 150)
    turtle.pensize(3)
    flyTo(-17, 200)
    turtle.seth(0)
    turtle.fillcolor("#ffffff")
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()
    flyTo(0, 0)


def drawFace():
    turtle.forward(183)
    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.left(45)
    turtle.circle(120, 100)
    turtle.seth(90)
    drawEye()
    turtle.seth(180)
    turtle.penup()
    turtle.fd(60)
    turtle.pendown()
    turtle.seth(90)
    drawEye()
    turtle.penup()
    turtle.seth(180)
    turtle.fd(64)
    turtle.pendown()
    turtle.seth(215)
    turtle.circle(120, 100)
    turtle.end_fill()


def drawHead():
    turtle.penup()
    turtle.circle(150, 40)
    turtle.pendown()
    turtle.fillcolor("#00a0de")
    turtle.begin_fill()
    turtle.circle(150, 280)
    turtle.end_fill()



def drawAll():

    drawHead()
    drawRedScarf()
    drawFace()
    drawRedNose()
    drawMouse()
    beard()
    flyTo(0, 0)
    turtle.seth(0)
    turtle.penup()
    turtle.circle(150, 50)
    turtle.pendown()
    turtle.seth(30)
    turtle.fd(40)
    turtle.seth(70)
    turtle.circle(-30, 270)
    turtle.fillcolor("#00a0de")
    turtle.begin_fill()
    turtle.seth(230)
    turtle.fd(80)
    turtle.seth(90)
    turtle.circle(1000, 1)
    turtle.seth(-89)
    turtle.circle(-1000, 10)
    turtle.seth(180)
    turtle.fd(70)
    turtle.seth(90)
    turtle.circle(30, 180)
    turtle.seth(180)
    turtle.fd(70)
    turtle.seth(100)
    turtle.circle(-1000, 9)
    turtle.seth(-86)
    turtle.circle(1000, 2)
    turtle.seth(230)
    turtle.fd(40)
    turtle.circle(-30, 230)
    turtle.seth(45)
    turtle.fd(81)
    turtle.seth(0)
    turtle.fd(203)
    turtle.circle(5, 90)
    turtle.fd(10)
    turtle.circle(5, 90)
    turtle.fd(7)
    turtle.seth(40)
    turtle.circle(150, 10)
    turtle.seth(30)
    turtle.fd(40)
    turtle.end_fill()

    turtle.seth(70)
    turtle.fillcolor("#FFFFFF")
    turtle.begin_fill()
    turtle.circle(-30)
    turtle.end_fill()

    flyTo(103.74, -182.59)
    turtle.seth(0)
    turtle.fillcolor("#FFFFFF")
    turtle.begin_fill()
    turtle.fd(15)
    turtle.circle(-15, 180)
    turtle.fd(90)
    turtle.circle(-15, 180)
    turtle.fd(10)
    turtle.end_fill()
    flyTo(-96.26, -182.59)
    turtle.seth(180)
    turtle.fillcolor("#FFFFFF")
    turtle.begin_fill()
    turtle.fd(15)
    turtle.circle(15, 180)
    turtle.fd(90)
    turtle.circle(15, 180)
    turtle.fd(10)
    turtle.end_fill()

    flyTo(-133.97, -91.81)
    turtle.seth(50)
    turtle.fillcolor("#FFFFFF")
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()

    flyTo(-103.42, 15.09)
    turtle.seth(0)
    turtle.fd(38)
    turtle.seth(230)
    turtle.begin_fill()
    turtle.circle(90, 260)
    turtle.end_fill()
    flyTo(5, -40)
    turtle.seth(0)
    turtle.fd(70)
    turtle.seth(-90)
    turtle.circle(-70, 180)
    turtle.seth(0)
    turtle.fd(70)

    flyTo(0, -150)
    drawBlackdrawEye()


def main():
    turtle.screensize(800, 6000, "#F0F0F0")
    turtle.pensize(3)
    turtle.speed(5)
    drawAll()


if __name__ == "__main__":
    main()
    turtle.mainloop()
