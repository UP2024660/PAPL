#-------------------------------------------------------------------------------
# Practical Worksheet 7: Booleans and while loops
# your name Mark Voss
# your student number UP2024660
#-------------------------------------------------------------------------------

from graphics import *
import time
import random
import math
from Week6 import calculateGrade


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
        mark = input("Please enter a number between 1 and 20 here: ")
        if mark.isdigit():
            mark = int(mark)
            calculateGrade(mark)
            break

#exercise4
def orderPrice():
    cont = True
    total =[]
    while cont:
        unitprice = float(input("How much is the product?: "))
        quantity = float(input("How many? "))
        quanUNI = unitprice * quantity
        total.append(quanUNI)
        again = input("Any more?: ")
        again = again.lower()
        if again in ["no","n"]:
            cont = False
            totalprice = sum(total)
            print("total price is {0:0.2f}".format(totalprice))


#exercise5
def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)


def drawBrownEyeInCentre(window, centre, radius):

    drawCircle(window,Point(250,250),100,"white")
    drawCircle(window,Point(250,250),50,"brown")
    drawCircle(window,Point(250,250),25,"black")

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

def clickableEye():
    win = GraphWin("brown eye",500,500)
    drawBrownEyeInCentre(win,Point(250,250),100)
    message = Text(Point(250,400), "")
    message.draw(win)
    centre = Point(250,250)

    while True:
        click = win.getMouse()
        mathY = distanceBetweenPoints(centre,click)
        if mathY >50 and mathY < 101:
            message.setText("sclera")
        elif mathY <51 and mathY >25:
            message.setText("iris")
        elif mathY <=25:
            message.setText("pupil")
        else:
            win.close()

# For exercise 6
def fahrenheit2Celsius(fahrenheit):
    celsius = ((fahrenheit -32) *5/9)
    print(celsius)
    return celsius


def celsius2Fahrenheit(celsius):
    fahrenheit = (9/5 * celsius +32)
    print(fahrenheit)
    return fahrenheit

def temperatureConverter():
    cont = True
    while cont:
        start = input("Fahrenheit to Celsius or Celsius to Fahrenheit?: ")
        start = start.lower()
        if start in ["fahrenheit","f"]:
            value = float(input("Please enter a temperature here: "))

            fahrenheit2Celsius(value)
        if start in ["celsius","c"]:
            value = float(input("Please enter a temperature here: "))
            celsius2Fahrenheit(value)
        decision = input("Would you like to stop? ")
        decision = decision.lower()
        if decision in ["yes","y"]:
            cont = False
        if decision in ["no","n"]:
            cont = True

#for exercise 7
def guessTheNumber():
    number = random.randint(1,100)
    guessesTaken = 0
    while guessesTaken < 7:
        userInput =int(input("Enter a number here: "))
        if userInput > number:
            print("Too high")
            guessesTaken = guessesTaken +1

        elif userInput == number:
            print("You win!")
            break
        else:
            print("too low")
            guessesTaken = guessesTaken +1
    if userInput != number:
        print("You lose! - the number was",number)


#exercise 8
def tableTennisScorer():
    win = GraphWin("TableTennis",500,500)
    line = Line(Point(250,0),Point(250,500))
    line.draw(win)
    player1 = 0
    player2 = 0
    cont = True

    title1 = Text(Point(125,50),"Player 1")
    title1.draw(win)
    title2 = Text(Point(375,50),"Player 2")
    title2.draw(win)

    player1msg = Text(Point(125,250),"")
    player1msg.draw(win)
    player2msg = Text(Point(375,250),"")
    player2msg.draw(win)

    while cont:

        click = win.getMouse()
        if click.getX() < 250:
            player1 += 1
        else:
            player2 += 1


        if (player1 >= 11 or player2 >= 11) and abs(player1 - player2) >=2:
            cont = False

        player1msg.setText(player1)
        player2msg.setText(player2)

    winner = Text(Point(125 if player1 > player2 else 375,400),"winner")
    winner.draw(win)
    win.getMouse()
    win.close()








'''

ALGORITHMS
python based Object detection
'''




