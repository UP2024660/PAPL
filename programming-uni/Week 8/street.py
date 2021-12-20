#-------------------------------------------------------------------------------
# house.py - a simple program to draw a house
#-------------------------------------------------------------------------------

from graphics import *

def getInputs():
    doorColour = input("Enter door colour: ")
    amountHouse = int(input("How many houses?: "))
    lightsYN = input("Are the lights on (y/n): ")
    lightsOn = lightsYN[0] == "y"
    winVSize = int(input("Enter Height: "))
    return doorColour,amountHouse, lightsOn, winVSize

def drawHouse(win, doorColour,amountHouse, lightsOn, winVSize,x,doorNum):
    #win = GraphWin("House", winSize, winSize)
    x = x
    roof = Polygon(Point(2 +x, 0.3*winVSize), Point(0.21*winVSize +x, 2),Point(0.79*winVSize +x, 2), Point(winVSize-2 +x,0.3*winVSize))
    roof.setFill("pink")
    roof.draw(win)

    # draw wall and door
    drawRectangle(win, Point(2 +x, 0.3*winVSize), Point(winVSize-2 +x, winVSize-2), "brown")
    drawRectangle(win, Point(0.15*winVSize +x, 0.55*winVSize), Point(0.4*winVSize +x, winVSize-2), doorColour)

    doorNumber = Text(Point(0.27*winVSize +x , 0.7*winVSize),doorNum)
    doorNumber.draw(win)

    # draw window
    if lightsOn:
        windowColour = "yellow"
    else:
        windowColour = "black"
    drawRectangle(win, Point((0.55*winVSize +x), (0.55*winVSize)), Point((0.85*winVSize +x), (0.85*winVSize)), windowColour)


def drawRectangle(win, point1, point2, colour):
    rectangle = Rectangle(point1, point2)
    rectangle.setFill(colour)
    rectangle.setOutline(colour)
    rectangle.draw(win)

def main():
    doorColour,amountHouse, lightsOn, winVSize = getInputs()
    win = GraphWin("House", winVSize*amountHouse, winVSize)
    amountHouse = amountHouse
    x = 0
    doorNum = 1
    for i in range(amountHouse):
        drawHouse(win,doorColour,amountHouse, lightsOn, winVSize ,x,doorNum)
        x += winVSize
        doorNum +=1
    win.getMouse()
    win.close()



main()
