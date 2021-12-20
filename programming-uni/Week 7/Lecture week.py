
from graphics import *
import math
from math import *




'''for i in range(4):
    for j in range(1, 5):
        print(i, j, "hello")
for k in range(10, 1, -2):
    print(k, "bye")'''


def mystery2(s, n):
    for ch in s:
        print(ch * n, end="")

def mystery3(s):
    for i in range(len(s)):
        print(" " * i + s[i])


def mystery4(n):
    x = 0
    for y in n:
        x = x + int(y)
    print(x)

def mystery5(n):
    for i in range(n):
        for j in range(i+1):
            print("#", end="")
        print()


def circles():
    win = GraphWin("Circles", 600,600)
    for i in range(15):
        mouse = win.getMouse()
        X = mouse.getX()
        Y = mouse.getY()
        circle = Circle(Point(X,Y), 30)
        if X < 300 and Y < 300:
            circle.setOutline("blue")
        elif X < 300 and Y > 300:
            circle.setOutline("pink")
        elif X > 300 and Y < 300:
            circle.setFill("blue")
        elif X > 300 and Y > 300:
            circle.setFill("pink")
        circle.draw(win)
    win.getMouse()
    win.close()


def circles2():
    win = GraphWin("Circles", 600,600)
    x  = 30
    y = 450
    for i in range(30):
        mouse = win.getMouse()
        X = mouse.getX()
        Y = mouse.getY()
        circle = Circle(Point(x,y),30)
        if X < 300 and Y < 300:
            circle.setOutline("blue")
        elif X < 300 and Y > 300:
            circle.setOutline("pink")
        elif X > 300 and Y < 300:
            circle.setFill("blue")
        elif X > 300 and Y > 300:
            circle.setFill("pink")
        circle.draw(win)
        x  += 60
        if x >600:
            x = 30
            y = y + 60
    win.getMouse()
    win.close()







