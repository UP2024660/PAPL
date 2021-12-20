#-------------------------------------------------------------------------------
# Practical Worksheet 7: Booleans and while loops
# your name
# your student number
#-------------------------------------------------------------------------------

from graphics import *
import time
import Week6.py
from Week6.py import calculateGrade



#exercise 1
def getName():
    while True:
        name = input("Please enter a name here: ")
        if name.isalpha():
            return name



# For exercise 2
def trafficLights():
    win = GraphWin()
    red = Circle(Point(100, 50), 20)
    red.setFill("red")
    red.draw(win)
    amber = Circle(Point(100, 100), 20)
    amber.setFill("black")
    amber.draw(win)
    green = Circle(Point(100, 150), 20)
    green.setFill("black")
    green.draw(win)
    while True:
        time.sleep(5)
        amber.setFill("yellow")
        time.sleep(5)
        red.setFill("black")
        amber.setFill("black")
        green.setFill("green")
        time.sleep(5)
        green.setFill("black")
        amber.setFill("yellow")
        time.sleep(5)
        amber.setFill("black")
        red.setFill("red")

#exercise 3
def gradeCoursework():
    while True:
        mark = int(input("Please enter a number between 1 and 20 here: "))
        if mark.isdigit():
            calculateGrade(mark)






# For exercise 6
def fahrenheit2Celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def celsius2Fahrenheit(celsius):
    return 9 / 5 * celsius + 32
