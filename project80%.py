from graphics import *
import winsound
import math
def archery():
    winsound.PlaySound('C://123.wav',winsound.SND_FILENAME)

    win = GraphWin("Archery Game", 500,500)
    win.setCoords(-50, -50, 50, 50)

    circle1 = Circle(Point(0,0), 40)
    circle1.setFill("white")
    circle1.draw(win)

    circle2 = Circle(Point(0,0), )
    circle2.setFill("black")
    circle2.draw(win)

    circle3 = Circle(Point(0,0),32)
    circle3.setFill("blue")
    circle3.draw(win)

    circle4 = Circle(Point(0,0),)
    circle4.setFill("red")
    circle4.draw(win)

    circle5 = Circle(Point(0,0),8)
    circle5.setFill("red")
    circle5.draw(win)

    score = 0

    for i in range(5):
        p = win.getMouse()
        p.draw(win)
        x = p.getX()
        y = p.getY()

        d = math.sqrt((x**2 + y**2))

        if 40 >= d > 35:
            score = score + 1

        elif 35 >= d > 30:
            score = score + 3

        elif 30 >= d > 25:
            score = score + 5

        elif 25 >= d > 20:
            score = score + 7

        elif 20 >= d >= 0:
            score = score + 9
        else:
            score = score + 0

        print("Your current score is:", score)

    win.getMouse()
    win.close()
archery()
