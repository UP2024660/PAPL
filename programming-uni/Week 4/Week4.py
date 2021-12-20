#Mark Voss, UP2024660



import math
from math import *

import graphics

from graphics import *

def main():

  def personalGreeting():
    name = input("Please enter your name: ")
    print("Hello "+name+", nice to see you!")

  personalGreeting()

  def formalName():
    name = input("Please enter your first and last name: ")
    first = name[0]
    sur = name.split(" ")
    sur = str(sur[1])
    print(first+".",sur)

  formalName()

  def kilos2pounds():
    userKilo = float(input("Please enter an amount in Kilograms: "))
    pounds = (userKilo * 2.20462)
    userKilo = str(userKilo)
    pounds = str(pounds)
    print("{0:0.2f} Kilos is equal to  {1:0.2f} Pounds ".format(float(userKilo), float(pounds)))

  kilos2pounds()

  def generateEmail():
    fname = str(input("Please enter your first name here: "))
    fname = fname.lower()
    lname = str(input("Please enter your surname here: "))
    lname = lname.lower()
    year = int(input("Please enter the last two digits of your year of study: "))
    year = str(year)
    print(lname[0:4]+"."+fname[0]+"."+year+"@myport.ac.uk")

  generateEmail()


  def gradeTest():
    score = int(input("Please enter the score of the test here: "))
    grade = "FFFFCCBBAAA"
    print("The grade is",grade[score])

  gradeTest()


  def graphicLetters():
    word = input("Please enter a word here: ")
    win = GraphWin("Graphic Letters", 200,200)
    p = win.getMouse()
    newmessage = Text(Point(p.getX(),p.getY())," ")
    newmessage.draw(win)


  #graphicLetters()


  def singASong():
    word = input("Please enter a word: ")
    lines = int(input("Please enter the amount of lines you want: "))
    reps = int(input("Please enter the amount of repetitions: "))
    print((((word + " ")*reps +'\n')*lines)[:-1])


  singASong()

  def exchangeTable():
    #1.10 euro to 1 po
    for i in range(21):

      euro = i * 1.10
      print(" {0:0.2f} |  {1:0.2f} \n".format(  i,  euro))

  exchangeTable()

  def makeInitialism():
    initi= input("Please enter a phrase: ")
    initi = initi.split(" ")
    list = []
    for i in range(len(initi)):
      word = initi[i]
      word = word[0].upper()
      list.append(word)
      print(word[0].upper(), end = "")
    print("\n")

  makeInitialism()

  def toNumber():
    name = input("Please enter your name here: ")
    name = name.lower()
    list = []
    for i in name:
      print(f"{i=}")
      value = (ord(i)-96)
      print(value)
      list.append(value)

    sum_list = sum(list)
    print(name, " has the value of", sum_list)
  toNumber()




#main()

def fileInCaps():

  output = input("Please enter a filename here: ")
  file1 = (output,".txt")

  with open(file1,"w") as file:
    print("Write a fileInCaps function which displays the contents of a file in capital letters.The name of the input file should be entered by the user", file = file1)
    file1.close()
  with open(file1, "r") as file:
    contents = file1.read()
    file1.close()
  print(contents.upper())

fileInCaps()




