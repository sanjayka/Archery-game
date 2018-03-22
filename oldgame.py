from graphics import *
import winsound
import math
def archery():
    win = GraphWin("Archery Game", 1600,1600)
    win.setCoords(-80, -80, 80, 80)

    rect = Rectangle(Point(-80,80),Point(80,0))
    rect.setFill("lightpink")
    rect.draw(win)

    rect1 = Rectangle(Point(-80,-80),Point(80,37))
    rect1.setFill("lightblue")
    rect1.draw(win)

    arrowimage = Image(Point(60,58), 'C:/archery/blind1.ppm')
    arrowimage.draw(win)

    arrowimage1 = Image(Point(-60,58), 'C:/archery/board.ppm')
    arrowimage1.draw(win)

    arrowimage1 = Image(Point(0,0), 'C:/archery/grass.ppm')
    arrowimage1.draw(win)

    rect1 = Rectangle(Point(-30,30),Point(30,-30))
    rect1.setFill("lightgreen")
    rect1.draw(win)

    circle1 = Circle(Point(0,0), 26)
    circle1.setFill("white")
    circle1.draw(win)

    circle2 = Circle(Point(0,0),20)
    circle2.setFill("black")
    circle2.draw(win)

    circle3 = Circle(Point(0,0),15)
    circle3.setFill("lightblue")
    circle3.draw(win)

    circle4 = Circle(Point(0,0),10)
    circle4.setFill("red")
    circle4.draw(win)

    circle5 = Circle(Point(0,0),6)
    circle5.setFill("yellow")
    circle5.draw(win)

    circle6 = Circle(Point(0,0),23)
    circle6.draw(win)

    circle7 = Circle(Point(0,0),17.5)
    circle7.setOutline('white')
    circle7.draw(win)

    circle8 = Circle(Point(0,0),12.5)
    circle8.draw(win)

    circle9 = Circle(Point(0,0),8)
    circle9.draw(win)

    circle10 = Circle(Point(0,0),2.5)
    circle10.draw(win)

    circle11 = Circle(Point(0,0),4.5)
    circle11.draw(win)

    line=Line(Point(0,1.5),Point(0,-1.5))
    line.draw(win)

    line=Line(Point(-1.5,0),Point(1.5,0))
    line.draw(win)


    score = 0

    for i in range(5):
        p = win.getMouse()
        x = p.getX()
        y = p.getY()
        line=Line(Point(x-1,y),Point(x+1,y))
        line.draw(win)
        line=Line(Point(x,y-1),Point(x,y+1))
        line.draw(win)

        d = math.sqrt((x**2 + y**2))
        if 26 >= d > 20:
            score = score + 1
            a="Score:"+str(score)
            inputBox = Entry(Point(-5,70), 8)
            inputBox.setText(a)
            inputBox.setTextColor("red")
            inputBox.setSize(30)
            inputBox.setFace("times roman")
            inputBox.draw(win)
            if i==4:
                winsound.PlaySound('C:/archery/lastshot.wav',winsound.SND_FILENAME)
            else:
                winsound.PlaySound('C:/archery/needmorepractice.wav',winsound.SND_FILENAME)

        elif 20 >= d > 15:
            score = score + 2
            a="Score:"+str(score)
            inputBox = Entry(Point(-5,70), 8)
            inputBox.setText(a)
            inputBox.setTextColor("red")
            inputBox.setSize(30)
            inputBox.setFace("times roman")
            inputBox.draw(win)
            if i==4:
                winsound.PlaySound('C:/archery/lastshot.wav',winsound.SND_FILENAME)
            else:
                winsound.PlaySound('C:/archery/needmorepractice.wav',winsound.SND_FILENAME)

        elif 15 >= d > 10:
            score = score + 4
            a="Score:"+str(score)
            inputBox = Entry(Point(-5,70), 8)
            inputBox.setText(a)
            inputBox.setTextColor("red")
            inputBox.setSize(30)
            inputBox.setFace("times roman")
            inputBox.draw(win)
            if i==4:
                winsound.PlaySound('C:/archery/lastshot.wav',winsound.SND_FILENAME)
            else:
                winsound.PlaySound('C:/archery/welltried.wav',winsound.SND_FILENAME)

        elif 10 >= d > 6:
            score = score + 6
            a="Score:"+str(score)
            inputBox = Entry(Point(-5,70), 8)
            inputBox.setText(a)
            inputBox.setTextColor("red")
            inputBox.setSize(30)
            inputBox.setFace("times roman")
            inputBox.draw(win)
            if i==4:
                winsound.PlaySound('C:/archery/lastshot.wav',winsound.SND_FILENAME)
            else:
                winsound.PlaySound('C:/archery/welltried.wav',winsound.SND_FILENAME)

        elif 6 >= d >= 2.5:
            score = score + 8
            a="Score:"+str(score)
            inputBox = Entry(Point(-5,70), 8)
            inputBox.setText(a)
            inputBox.setTextColor("red")
            inputBox.setSize(30)
            inputBox.setFace("times roman")
            inputBox.draw(win)
            if i==4:
                winsound.PlaySound('C:/archery/lastshot.wav',winsound.SND_FILENAME)
            else:
                winsound.PlaySound('C:/archery/niceshot.wav',winsound.SND_FILENAME)
            
            
        elif 2.5 >= d:
            score = score + 10
            a="Score:"+str(score)
            inputBox = Entry(Point(-5,70), 8)
            inputBox.setText(a)
            inputBox.setTextColor("red")
            inputBox.setSize(30)
            inputBox.setFace("times roman")
            inputBox.draw(win)
            if i==4:
                winsound.PlaySound('C:/archery/lastshot.wav',winsound.SND_FILENAME)
            else:
                winsound.PlaySound('C:/archery/niceshot.wav',winsound.SND_FILENAME)
            
        else:
            score = score + 0
            a="Score:"+str(score)
            inputBox = Entry(Point(-5,70), 8)
            inputBox.setText(a)
            inputBox.setTextColor("red")
            inputBox.setSize(30)
            inputBox.setFace("times roman")
            inputBox.draw(win)
            if(-80 <= x <= -30 and 30 <= y <= 80):
                if i==4:
                   winsound.PlaySound('C:/archery/lastshot.wav',winsound.SND_FILENAME)
                else:
                   winsound.PlaySound('C:/archery/rightanddownwards.wav',winsound.SND_FILENAME)
            elif(-80 <= x <= -30 and -80 <= y <= -30):
                if i==4:
                   winsound.PlaySound('C:/archery/lastshot.wav',winsound.SND_FILENAME)
                else:
                   winsound.PlaySound('C:/archery/rightandupwards.wav',winsound.SND_FILENAME)
            elif(30 <= x <= 80 and -80 <= y <= -30):
                if i==4:
                   winsound.PlaySound('C:/archery/lastshot.wav',winsound.SND_FILENAME)
                else:
                   winsound.PlaySound('C:/archery/leftandupwards.wav',winsound.SND_FILENAME)
            elif(30 <= x <= 80 and 30 <= y <= 80):
                if i==4:
                   winsound.PlaySound('C:/archery/lastshot.wav',winsound.SND_FILENAME)
                else:
                   winsound.PlaySound('C:/archery/leftanddownwards.wav',winsound.SND_FILENAME)
            elif(-80 <= x <= -30 and -30 <= y <= 30):
                if i==4:
                   winsound.PlaySound('C:/archery/lastshot.wav',winsound.SND_FILENAME)
                else:
                   winsound.PlaySound('C:/archery/right.wav',winsound.SND_FILENAME)
            elif(-30 <= x <= 30 and -80 <= y <= -30):
                if i==4:
                   winsound.PlaySound('C:/archery/lastshot.wav',winsound.SND_FILENAME)
                else:
                   winsound.PlaySound('C:/archery/upwards.wav',winsound.SND_FILENAME)
            elif(30 <= x <= 80 and -30 <= y <= 30):
                if i==4:
                   winsound.PlaySound('C:/archery/lastshot.wav',winsound.SND_FILENAME)
                else:
                   winsound.PlaySound('C:/archery/left.wav',winsound.SND_FILENAME)
            elif(-30 <= x <= 30 and 30 <= y <= 80):
                if i==4:
                   winsound.PlaySound('C:/archery/lastshot.wav',winsound.SND_FILENAME)
                else:
                   winsound.PlaySound('C:/archery/downwards.wav',winsound.SND_FILENAME)
            else:
                if i==4:
                   winsound.PlaySound('C:/archery/lastshot.wav',winsound.SND_FILENAME)
                else:
                   winsound.PlaySound('C:/archery/regionoftarget.wav',winsound.SND_FILENAME)

        print("Your current score is:", score)

    win.getMouse()
    win.close()
archery()
