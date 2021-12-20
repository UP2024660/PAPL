#-------------------------------------------------------------------------------
# Practical Worksheet 5: Using functions
# your name Mark Voss
# your student number UP2024660
#-------------------------------------------------------------------------------
import graphics
from graphics import *
import math


# For exercises 1 and 2
def areaOfCircle(radius):
    return math.pi * radius ** 2

def circumferenceOfCircle(radius):
    return math.pi * (radius * 2)


def circleInfo():
    radius = int(input("Please enter the radius: "))
    areaOfCircle(radius)
    area = areaOfCircle(radius)
    circ = circumferenceOfCircle(radius)
    print("The area is {0:0.3f} and the circumference is {1:0.3f}".format(float(area), float((circ))))


# For exercise 3
def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)



def drawBrownEyeInCentre(window, centre, radius):
    window = GraphWin()
    drawCircle(window,Point(100,100),40,"white")
    drawCircle(window,Point(100,100),20,"brown")
    drawCircle(window,Point(100,100),10,"black")
    window.getMouse()
    window.close()

#drawBrownEyeInCentre()

def drawBlockOfStars(width,height):
    return print(((("*")*width + '\n') * height)[:-1])

#drawBlockOfStars()


def drawLetterE():
    drawBlockOfStars(8,2)
    drawBlockOfStars(2,2)
    drawBlockOfStars(5,2)
    drawBlockOfStars(2,2)
    drawBlockOfStars(8,2)

# For exercise 5
def drawBrownEye(win, centre, radius):
    BigCircle = drawCircle(win,centre,radius,"white")
    MiddleCircle = drawCircle(win,centre,radius/2,"brown")
    SmallCircle = drawCircle(win,centre,radius/4,"black")

    return BigCircle,MiddleCircle,SmallCircle




def drawPairOfBrownEyes():
    win = GraphWin("Draw Eyes",500,500)

    drawBrownEye(win,Point(190,250),60)
    drawBrownEye(win,Point(310,250),60)
    win.getMouse()
    win.close()


def distanceBetweenPoints(Point,Point2):
    #Pythagoras c^2 = A^2 + B^2
    # a is x2 - x1
    # b is y2 - y1
    #c is Sq.rt (a^2 + b^2)
    a = Point.getX()
    b = Point.getY()
    c = Point2.getX()
    d = Point2.getY()
    anew = int(Point2.getX() - Point.getX())
    bs = int(Point2.getY() - Point.getY())
    asqr = anew ** 2
    bsqr = bs ** 2
    csqr = asqr +bsqr
    c = math.sqrt(csqr)
    return c

def drawBlocks(space,width,space1,width1,height):
    for i in range(height):
        print(space * " " + width * "*" + space1 * " " + width1 * "*")

def drawLetterA():
    (drawBlocks(1,8,0,0,2))
    (drawBlocks(0,2,6,2,2))
    (drawBlocks(0,10,0,0,2))
    (drawBlocks(0,2,6,2,3))


def drawFourPairsOfBrownEyes():
    win = GraphWin()
    for i in range(4):
        centre = win.getMouse()
        radius = win.getMouse()
        c = distanceBetweenPoints(centre,radius)
        rightCentre = Point(centre.getX() + c *2 , centre.getY())
        drawBrownEye(win, centre, c)
        drawBrownEye(win, rightCentre,c)
    win.getMouse()
    win.close()



