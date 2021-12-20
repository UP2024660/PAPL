from graphics import *
import math
from math import *
colours= ["blue","yellow","orange","red","green","grey","purple","black"]

def drawPatch(win,x,y,colour):
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

def drawPatchwork(win,size,colour):
    x =0
    y = 0
    for i in range(size):
        for j in range(size):
            drawPatch(win,x,y,colour)
            x += 100
        x = (0)
        y = y + 100

def drawHoRectangle(win,colour,x,y,i):
    p1 = Point(x,y+(i*5))
    p2 = Point(x+20,y+(i+1)*5)
    rectangle = Rectangle(p1,p2)
    rectangle.setFill(colour)
    rectangle.draw(win)

def drawVeRectangle(win,colour,x,y,i):
    p1 = Point(x+(i*5),y)
    p2 = Point(x+((i+1)*5),y+20)
    rectangle = Rectangle(p1,p2)
    rectangle.setFill(colour)
    rectangle.draw(win)

def drawWHRectangle(win,colour1,x0,y0):
    myBool = True
    y = y0 + 20
    for a in range(2):
        x = x0+0
        for b in range(3):
            for i in range(4):
                if myBool:
                    colour = "white"
                else:
                    colour = colour1
                drawHoRectangle(win,colour,x,y,i)
                myBool = not myBool
            x +=40
        y += 40

def drawRHRectangle(win,colour1,x0,y0):
    myBool = True
    y = y0 +0
    for a in range(3):
        x = x0 + 20
        for b in range(2):
            for i in range(4):
                if myBool:
                    colour = colour1
                else:
                    colour = "white"
                drawHoRectangle(win,colour,x,y,i)
                myBool = not myBool
            x +=40
        y += 40

def drawRVertRectangle(win,colour1,x0,y0):
    myBool = True
    y = y0 + 0
    for a in range(3):
        x = x0 + 0
        for b in range(3):
            for i in range(4):
                if myBool:
                    colour = colour1
                else:
                    colour = "white"
                drawVeRectangle(win,colour,x,y,i)
                myBool = not myBool
            x +=40
        y = y +40

def drawWVertRectangle(win,colour1,x0,y0):
    myBool = True
    y = y0 +20
    for a in range(2):
        x = x0 + 20
        for b in range(2):
            for i in range(4):
                if myBool:
                    colour = "white"
                else:
                    colour = colour1
                drawVeRectangle(win,colour,x,y,i)
                myBool = not myBool
            x +=40
        y = y +40

def drawSecondPatch(win,x,y,colour):
    drawWHRectangle(win,colour,x,y)
    drawRVertRectangle(win,colour,x,y)
    drawRHRectangle(win,colour,x,y)
    drawWVertRectangle(win,colour,x,y)

def sides(win,size,colour,colour2,colour3):
    winSize = size*100
    if size == 5 or size == 7:
        drawPatchwork(win,size,colour)
        x = 0
        y = 100
        for i in range(size-2):
            drawSecondPatch(win,x,y,colour2)
            y += 100

        x = 100
        y = 200
        for i in range(size-4):
                drawSecondPatch(win,x,y,colour2)
                y += 100

        x = winSize - 100
        y = 100
        for i in range(size -2):
            drawSecondPatch(win,x,y,colour3)
            y += 100

        x = winSize - 200
        y = 200
        for i in range(size -4):
            drawSecondPatch(win,x,y,colour3)
            y += 100

        if size == 7:
            x = 200
            y = 300
            drawSecondPatch(win,x,y,colour2)
            x = 400
            y = 300
            drawSecondPatch(win,x,y,colour3)

def drawTotal():
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
                        win = GraphWin("Patchwork", 100*size ,100*size, autoflush = False)
                        sides(win,size,colour,colour2,colour3)
                        win.getMouse()
                        win.close()