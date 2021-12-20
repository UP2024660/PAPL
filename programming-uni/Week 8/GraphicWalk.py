from graphics import *

def drawLine(win,x,y,x2,y2):
    line = Line(Point(x,y),Point(x2,y2))
    x = x2
    y = y2
    line.setOutline("black")
    line.draw(win)
    return x , y

def drawBoundary(win,area):
    centre_x = area/2
    centre_y = area/2
    boundary = Circle(Point(centre_x,centre_y),area/2)
    boundary.setOutline("black")
    boundary.draw(win)

def distanceAway(x, y):
    return (abs(x)**2 + abs (y))**0.5

def main():
    numWalks, numSteps, area = getInputs()
    win = GraphWin("GraphicWalk",area,area)
    centre = area/2
    x = area/2
    y = area/2
    drawBoundary(win,area)
    averageSteps = takeWalks(win,area,numWalks, numSteps,x,y)
    printExpectedDistance(averageSteps)
    win.getMouse()
    win.close()



def getInputs():
    numWalks = int(input("How many random walks to take? "))
    numSteps = int(input("How many steps for each walk? "))
    area = int(input("Please enter the Boundary distance: "))
    return numWalks, numSteps, area

def takeWalks(win,area,numWalks, numSteps,x,y):
    totalSteps = 0
    for walk in range(numWalks):
        stepsAway = takeAWalk(win,area,numSteps,x,y)
        totalSteps += stepsAway
    return totalSteps / numWalks

def printExpectedDistance(averageSteps):
    print("The expected number of steps away from the", end=" ")
    print(f"start point is, {averageSteps:.5f}")


def takeAWalk(win,area, numSteps,x,y):
    from random import random
    stepsForwardOfStartX = 0
    stepsForwardOfStartY = 0
    Startx = area/2
    Starty = area/2
    for step in range(numSteps):
        if random() < 0.5:
            if random() < 0.5:
                stepsForwardOfStartX -= 1
                drawLine(win,Startx,Starty,x-5,y)
                x -= 5
            else:
                stepsForwardOfStartX =  step
                drawLine(win,x,y,x+5,y)
                x += 5
        else:
            if random() <0.5:
                stepsForwardOfStartY -= 1
                drawLine(win,x,y,x,y-5)
                y -= 5
            else:
                stepsForwardOfStartY = step
                drawLine(win,x,y,x,y+5)
                y += 5
    if  (x-(area/2))**2 + (y -(area/2))**2 > (area/2)**2:
        win.close()

    return distanceAway(stepsForwardOfStartX, stepsForwardOfStartY)

main()