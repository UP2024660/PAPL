from graphics import *
import math
from math import *
from repeat_test import *

colours= ["blue","yellow","orange","red","green","grey","purple","black"]


def drawPatch(win,x,y,colour):
    #win = GraphWin()
    x0 = x
    y0 = y
    x1 = x + 100
    y1 = y + 100
    for i in range(0,100,10):
        drawLine(win,Point(x0+i,y0), Point(x1-i,y1),colour)
        drawLine(win,Point(x0,y0+i), Point(x1,y1-i),colour)

def drawLine(win,p1,p2,colour):
        line = Line(p1, p2)
        line.setFill(colour)
        line.setOutline(colour)
        line.draw(win)

def drawPatchwork():
    win = GraphWin("Patchwork", 100*size,100*size, autoflush = False)
    x =0
    y = 0
    for i in range(size):
        for j in range(size):
            drawPatch(win,x,y,colour)
            x += 100
        x = (0)
        y = y + 100

    win.getMouse()
    win.close()


def main():
    cont = True
    while cont:
        size = int(input("Please enter size 5 for 5x5 or 7 for 7x7: "))
        if size == 5 or size ==7:
            colour = input("Please enter a colour here: ")
            if colour in colours:
                colour2 = input("please enter another colour here: ")
                if colour2 in colours:
                    colour3 = input("Please enter a final colour here: ")
                    if colour3 in colours and colour3 != colour2 or colour3 != colour:
                        cont = False
                        def drawPatchwork():
                            win = GraphWin("Patchwork", 100*size,100*size, autoflush = False)
                            x =0
                            y = 0
                            for i in range(size):
                                for j in range(size):
                                    drawPatch(win,x,y,colour)
                                    x += 100
                                x = (0)
                                y = y + 100
                            drawSecondPatch(win,x,y,colour)
                            win.getMouse()
                            win.close()
                        drawPatchwork()
                    else:
                        cont = True

    else:
        cont = True


main()