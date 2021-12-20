from graphics import *


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

def drawSecondPatch(x,y,colour,size):
    win = GraphWin("Patchwork", 100*size ,100*size, autoflush = False)
    drawWHRectangle(win,colour,x,y)
    drawRVertRectangle(win,colour,x,y)
    drawRHRectangle(win,colour,x,y)
    drawWVertRectangle(win,colour,x,y)



def main():
    size = int(input("please enter: "))
    drawSecondPatch(0,0,"red",size)

main()