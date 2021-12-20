#-------------------------------------------------------------------------------
# house.py - a simple program to draw a house
#-------------------------------------------------------------------------------

from graphics import *

def getInputs():
    doorColour = input("Enter door colour: ")
    lightsYN = input("Are the lights on (y/n): ")
    lightsOn = lightsYN[0] == "y"
    winSize = int(input("Enter graphics window size: "))
    doorNum = int(input("Enter door number: "))
    return doorColour, lightsOn, winSize, doorNum

def drawHouse(doorColour, lightsOn, winSize, doorNum):
    win = GraphWin("House", winSize, winSize)
    roof = Polygon(Point(2, 0.3*winSize), Point(0.21*winSize, 2), Point(0.79*winSize, 2), Point(winSize-2,0.3*winSize))
    roof.setFill("pink")
    roof.draw(win)
    # draw wall and door
    drawRectangle(win, Point(2, 0.3*winSize), Point(winSize-2, winSize-2), "brown")
    drawRectangle(win, Point(0.15*winSize, 0.55*winSize), Point(0.4*winSize, winSize-2), doorColour)
    doorNumber = Text(Point(0.27*winSize, 0.7*winSize), doorNum)
    doorNumber.draw(win)
    # draw window
    if lightsOn:
        windowColour = "yellow"
    else:
        windowColour = "black"
    drawRectangle(win, Point(0.55*winSize, 0.55*winSize), Point(0.85*winSize, 0.85*winSize), windowColour)
    win.getMouse()
    win.close()

def drawRectangle(win, point1, point2, colour):
    rectangle = Rectangle(point1, point2)
    rectangle.setFill(colour)
    rectangle.setOutline(colour)
    rectangle.draw(win)

def main():
    doorColour, lightsOn, winSize, doorNum = getInputs()
    drawHouse(doorColour, lightsOn, winSize, doorNum)



main()
