import graphics
from graphics import *
import math

#9
def drawPatchWindow():
    win = GraphWin("Patch",200,200)

    x0 = 0
    y0 = 0
    x1 = 100
    y1 = 100

    for i in range(5):
        line = Line(Point(x0,y0+20), Point(x1,y0+20))
        line.setOutline("red")
        line.draw(win)
        y0 += (20)

    x0 = 0
    y0 = 0
    x1 = 100
    y1 = 100
    for i in range(5):
        line = Line(Point(x0+20,y0), Point(x0+20,y1))
        line.setOutline("red")
        line.draw(win)
        x0 += (20)

    x = 10
    y = 10
    for i in range(5):
        for j in range(5):
            message = Text(Point(x,y),"hi!")
            message.setOutline("red")
            message.draw(win)
            x += 20
        x = (10)
        y = y +20


    win.getMouse()
    win.close()


# 10
def drawPatch(win,x,y,colour):
    x0 = x
    y0 = y
    x1 = x + 100
    y1 = y + 100

    for i in range(5):
        line = Line(Point(x0,y0+20), Point(x1,y0+20))
        line.setOutline("red")
        line.draw(win)
        y0 += (20)

    x0 = x
    y0 = y
    x1 = x + 100
    y1 = y + 100
    for i in range(5):
        line = Line(Point(x0+20,y0), Point(x0+20,y1))
        line.setOutline("red")
        line.draw(win)
        x0 += (20)

    x = x + 10
    y = y + 10

    for i in range(5):
        for j in range(5):
            message = Text(Point(x,y),"hi!")
            message.setOutline("red")
            message.draw(win)
            x += 20
            #y += 20
        x = (10)
        y += 20



def drawPatchWork():
    win = GraphWin("Patchwork", 300,200)
    x = 0
    y = 0
    for i in range(10):
        for j in range(3):
            drawPatch(win,x,y,"blue")
            x += 100
        x = (0)
        y += 20
    win.getMouse()
    win.close()








