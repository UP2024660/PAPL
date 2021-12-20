from graphics import *

win = GraphWin("Patchwork", 200 ,200, autoflush = False)
# for loop for each horizontal line
'''
RedV = True
RedH = True
WhiteH = True
WhiteV = True




myBool = True
x = 0
y = 0
a = 5
b = 20
'''
def drawRectangle(win,colour,a,b):
    rectangle = Rectangle(Point(x,y),Point(x+a,y+b))
    rectangle.setFill(colour)
    rectangle.draw(win)


'''
x = 0
for i in range(5):
    x = 0
    for j in range(5):
        if re
        for k in range(4):
            if myBool:
                colour = "red"
            else:
                colour = "white"
            drawRectangle(win,colour,5,20)
            myBool = not myBool
            x+=5
        #x +=40
win.getMouse()
win.close()
'''

x =0
y = 0
a = 5
b = 20
myBool = True
myFlower = True

for i in range(4):
    if myBool:
        colour = "red"
    else:
        colour = "white"

    if myFlower:
        drawRectangle(win,colour,a,b)
        myBool = not myBool
        x +=5
        print("a")
        myFlower = not myFlower
    else:
        myFlower = not myFlower
        x = 20
        y = 0
        a = 20
        b = 5
        drawRectangle(win,colour,a,b)
        y +=5


win.getMouse()
win.close()




'''
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
'''

def drawRedVerticalRectangle(win,x,y,colour):
    x = 0
    y = 20
    for i in range(3):
        for a in range(3):
            for b in range(2):
                rectangle = Rectangle(Point(x,y-20),Point(x+5,y))
                rectangle.setFill(colour)
                rectangle.draw(win)
                rectangle = Rectangle(Point(x+5,y-20),Point(x+10,y))
                rectangle.setFill("white")
                rectangle.draw(win)
                x = x +10
            x +=20
        x = (0)
        y = y +40






def drawRedHorizontalRectangle(win,x,y,colour):
    #redhorizontal
    x = 20
    y =0
    for i in range(3):
        for b in range(2):
            rectangle = Rectangle(Point(x,y),Point(x+20,y+5))
            rectangle.setFill(colour)
            rectangle.draw(win)
            rectangle = Rectangle(Point(x,y+5),Point(x+20,y+10))
            rectangle.setFill("white")
            rectangle.draw(win)
            y = y +10
        y = y+20

    y = 0
    x = 60
    for a in range(3):
        for b in range(2):
            rectangle = Rectangle(Point(x,y),Point(x+20,y+5))
            rectangle.setFill(colour)
            rectangle.draw(win)
            rectangle = Rectangle(Point(x,y+5),Point(x+20,y+10))
            rectangle.setFill("white")
            rectangle.draw(win)
            y = y+10
        y = y + 20

def drawWhiteVerticalRectangle(win,x,y,colour):
    #white vertical
    x = 20
    y = 20
    for i in range(2):
        for a in range(2):
            for b in range(2):
                rectangle = Rectangle(Point(x,y),Point(x+5,y+20))
                rectangle.setFill("white")
                rectangle.draw(win)
                rectangle = Rectangle(Point(x+5,y),Point(x+10,y+20))
                rectangle.setFill(colour)
                rectangle.draw(win)
                x = x +10
            x += 20
        x = (20)
        y = y+40


def drawWhiteHorizontalRectangle(win,x,y,colour):

#whitehorizontal
    x =0
    y =20
    y1 = 40

    for a in range(3):
        y = 20
        for b in range(2):
            rectangle = Rectangle(Point(x,y),Point(x+20,y+5))
            rectangle.setFill("white")
            rectangle.draw(win)
            rectangle = Rectangle(Point(x,y+5),Point(x+20,y+10))
            rectangle.setFill(colour)
            rectangle.draw(win)
            y = y+10
        x = x + 40
    x =0
    for a in range(3):
        y = 60
        for b in range(2):
            rectangle = Rectangle(Point(x,y),Point(x+20,y+5))
            rectangle.setFill("white")
            rectangle.draw(win)
            rectangle = Rectangle(Point(x,y+5),Point(x+20,y+10))
            rectangle.setFill(colour)
            rectangle.draw(win)
            y = y+10
        x = x + 40



def drawSecondPatch():
    win = GraphWin("Patchwork", 200 ,200, autoflush = False)

    x = 0
    y =20
    drawRedVerticalRectangle(win,x,y,"red")

    x = 20
    y =0
    drawRedHorizontalRectangle(win,x,y,"red")

    x =0
    y =20
    drawWhiteHorizontalRectangle(win,x,y,"red")

    x = 20
    y = 20
    drawWhiteVerticalRectangle(win,x,y,"red")
    #drawRectangle(win,x,y,"red")'''
    win.getMouse()
    win.close()