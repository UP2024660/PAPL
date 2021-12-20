# Practical Worksheet P3: Graphical Programming
# your name, your number
# Mark Voss, 2024660


from graphics import *

from math import *


def drawStickFigure():
    win = GraphWin("Stick figure")
    head = Circle(Point(100, 60), 20)
    head.draw(win)
    body = Line(Point(100, 80), Point(100, 120))
    body.draw(win)
    arms = Line(Point(80, 100), Point(120, 100))
    arms.draw(win)
    left = Line(Point(100, 120), Point(75, 150))
    left.draw(win)
    right = Line(Point(100, 120), Point(125, 150))
    right.draw(win)
    win.getMouse()
    win.close()
#drawStickFigure()

def drawCircle():
    radius = int(input("Please enter the size of the radius: "))
    win = GraphWin("Circle")
    circle = Circle(Point(100,100), radius)
    circle.draw(win)
    win.getMouse()
    win.close()
#drawCircle()



def drawArcheryTarget():
    win= GraphWin("Archery")
    Blue = Circle(Point(100,100),60)
    Blue.draw(win)
    Blue.setFill("Blue")
    Red = Circle(Point(100,100),40)
    Red.draw(win)
    Red.setFill("Red")
    Yellow = Circle(Point(100,100), 20)
    Yellow.draw(win)
    Yellow.setFill("Yellow")
    win.getMouse()
    win.close()

#drawArcheryTarget()


def drawRectangle():
    
    height = int(input("Please enter the height: "))
    width = int(input("Please enter the width: "))
    win = GraphWin("Rectangle")
    topleftx = 100 - (width / 2 )
    toplefty = 100 + (height /  2)
    botrightx = 100 + (width / 2)
    botrighty = 100 - (height / 2)
    rectangle = Rectangle(Point(topleftx,toplefty), Point(botrightx, botrighty))
    rectangle.draw(win)
    win.getMouse()
    win.close()

#height = 20 , so top left would be (X , 110)
#Width = 40 , so top left would be (80, 110)
#bottom right, would be (120, 90)

#drawRectangle()    




def BlueCircle():
    win = GraphWin("Your Circle")
    point = win.getMouse()
    PointX = point.getX()
    PointY = point.getY()
    
    circle = Circle(Point(PointX, PointY), 50)
    circle.draw(win)
    circle.setFill("Blue")
    win.getMouse()
    win.close()

#BlueCircle()

def drawLine():
    win = GraphWin("Line drawer")
    for i in range(0,10):
        message = Text(Point(100,100), "Click on first point")
        message.draw(win)
        p1 = win.getMouse()
        message.setText("Click on second point")
        p2 = win.getMouse()
        line = Line(p1, p2)
        line.draw(win)
        message.setText("")
    win.getMouse()
    win.close()


#drawLine()

def tenStrings():
    win = GraphWin("Ten Strings",400,400)
    
    for i in range(0,10):
        message = Text(Point(200, 200), "Enter whatever you want & click mouse")
        message.draw(win)

        inputBox = Entry(Point(100, 100), 10)
        inputBox.draw(win)

        p = win.getMouse()
        newmessage = Text(Point(p.getX(), p.getY())," ")
        newmessage.draw(win)
        
        newmessage.setText( inputBox.getText())
    win.getMouse()
    win.close()

#tenStrings()


def tenColouredRectangles():
    win = GraphWin("Ten Rectangles",1000,1000)

    for i in range(0,10):
        message= Text(Point(500,400), "Enter the colour that you want your rectangle to be")
        message.draw(win)

        inputBox = Entry(Point(500,500), 10)
        inputBox.draw(win)

        topleft = win.getMouse()
        topleftX = topleft.getX()
        topleftY = topleft.getY()
        
        bottomright = win.getMouse()
        bottomrightX = bottomright.getX()
        bottomrightY = bottomright.getY()
        
        rectangle = Rectangle(Point(topleftX, topleftY), Point(bottomrightX, bottomrightY))
        rectangle.draw(win)
        rectangle.setFill(inputBox.getText() )
    win.getMouse()
    win.close()

#tenColouredRectangles()

def fiveClickStickFigure():
    import math
    win = GraphWin("Stick Figure", 1000,1000)
    for i in range(5):
        centre = win.getMouse()
        centreX = centre.getX()
        centreY = centre.getY()
    
    
        outC = win.getMouse()
        outCX = outC.getX()
        outCY = outC.getY()
            
        radiusQR = (((outCX - centreX) ** 2 ) + ((outCY - centreY)**2)) 
        radius = math.sqrt(radiusQR)
    
        circle = Circle(Point(centreX, centreY-radius), radius)
        
        circle.draw(win)
    
            
        point3 = win.getMouse()
        point3 = point3.getY()
    
        body = Line(Point(centreX,centreY),Point(centreX,point3))
        body.draw(win)
    
        point4 = win.getMouse()
        point4X = point4.getX()
        point4Y = point4.getY()
    
        hand = centreX - point4X
        arms = Line(Point(point4X, point4Y),Point(centreX + hand, point4Y))
        arms.draw(win)
    
        point5 = win.getMouse()
        point5X = point5.getX()
        point5Y = point5.getY()
    
        left = Line(Point(centreX,point3),Point(point5X,point5Y))
        left.draw(win)
    
        rightside = centreX - point5X 
        right = Line(Point(centreX,point3), Point(centreX + rightside, point5Y))
        right.draw(win)
    win.getMouse()
    win.close()
#fiveClickStickFigure()

'''
def plotRainfall():
'''













    
    
    
    
