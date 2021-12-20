#-------------------------------------------------------------------------------
# Practical Worksheet 6: if statements and for loops
# your name     Mark Voss
# your student number    2024660
#-------------------------------------------------------------------------------

from graphics import *
import math
from math import *


#1
def fastFoodOrderPrice():
    price = int(input("Please enter the price of your order: "))
    if price < 10:
        price = price + 1.50
    print("The total price of your order is: £{0:0.2f}".format(price))

#2
def whatToDoToday():
    temp = int(input("Please enter the current temperature: "))
    if temp > 25:
        print("You should probably swim in the sea")
    elif temp >= 10:
        print("Go shopping in Gunwharf")
    else:
        print("Stay at home and watch a film")
#3
def displaySquareRoots(start, end):
    for i in range(end - 1):
        print("The Square Root of",start,"is {0:0.3f}".format(math.sqrt(start)))
        start += 1

#4
def calculateGrade(mark):
    if mark >= 16 and mark < 21:
        print("A")
    elif mark >= 12 and mark < 16:
        print("B")
    elif mark >= 8 and mark < 12:
        print("C")
    elif mark <= 7 or mark == 0:
        print("F")
    else:
        print("X")

#5
def peasInAPod():
    peas = int(input("Please enter the number of peas: "))
    win = GraphWin("Peas in a Pod", peas * 100, 100)
    p = 50
    for i in range(peas + 1):
        pea = Circle(Point(p,50),50)
        pea.setFill("green")
        pea.draw(win)
        p+=100
    win.getMouse()
    win.close()

    # FOR I IN RANGE(50,pea*100,100)
#6
def ticketPrice(journeydist,age):
    ticket = float(3 + (journeydist * 0.15))
    if age <= 15 or age >=60:
        ticket = ticket * 0.6
    return ("{0:0.2f}".format(ticket))
#7
def numberedSquare(n):
    for i in range(n,0, -1):
        for j in range(i,i+n):
            print(j, end =" ")
        print()


# For exercises 8 & 11
def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)


# For exercise 8
def drawColouredEye(win, centre, radius, colour):
    drawCircle(win,centre,radius,"white")
    drawCircle(win,centre,radius/2,colour)
    drawCircle(win,centre,radius/4,"black")



def eyepicker(win, centre, radius , colour):
    if colour == "blue" or colour == "brown" or colour == "grey" or colour == "green":
        win = GraphWin()
        drawColouredEye(win,centre,radius,colour)
        win.getMouse()
        win.close()
    else:
        print("Not valid eye colour")

#9
def drawPatchWindow():
    win = GraphWin("Patch",200,200)
    x0 = 0
    y0 = 0
    x1 = 100
    y1 = 100
    for i in range(10):
        line = Line(Point(x0,y0), Point(x1,y1))
        line.setFill("red")
        line.setOutline("red")
        line.draw(win)
        x0 += (100/10)
        x1 -= (100/10)
    for i in range(10):
        line = Line(Point(x0,y0), Point(x1,y1))
        line.setFill("red")
        line.setOutline("red")
        line.draw(win)
        y0 += (100/10)
        y1 -= (100/10)

    win.getMouse()
    win.close()

#10
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
    win = GraphWin("Patchwork", 300,200)
    x =0
    y = 0
    for i in range(2):
        for j in range(3):
            drawPatch(win,x,y,"blue")
            x += 100
        x = (0)
        y = y + 100

    win.getMouse()
    win.close()


#11
def eyesAllAround():
    win = GraphWin("Eyes", 500,500)
    eye_colour_list = ["blue","grey","green","brown"]
    for i in range(0,30):
        centre = win.getMouse()
        drawColouredEye(win,centre,30, eye_colour_list[i%4])
    win.getMouse()
    win.close()









'''
colours =  ["blue","grey","green","brown"]

>>> colours[3]]
  File "<console>", line 1
    colours[3]]
              ^
SyntaxError: unmatched ']'

>>> colours[3]
'brown'

>>> x = 200

>>> y=100

>>> x+y
300

>>> colours[(x+y)//100%len(colours)]
'brown'

>>> y+=100

>>> colours[(x+y)//100%len(colours)]
'blue'
'''





