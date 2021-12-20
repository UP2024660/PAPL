import math


def CircumferenceofCircle():
    r = float(input("Please enter a value for your radius: "))
    Circ = 2* r * math.pi
    print("Circumference is",Circ)


#CircumferenceofCircle()

def areaofCircle():
    r = float(input("Please enter a value for your radius here: "))
    area = math.pi * r ** 2
    print("Area is",area)

#areaofCircle()


def costOfPizza():
    diameter = float(input("Please enter a diameter of your pizza here: "))
    radius = diameter / 2
    area = math.pi * radius **2
    cost = area *1.5
    print("Total cost of Pizza is",cost,"pence")


#costOfPizza()

def slopeOfLine():
    x1 = int(input("Please enter your first X value: "))
    y1 = int(input("Please enter your first Y value: "))
    x2 = int(input("Please enter your second X value: "))
    y2 = int(input("Please enter your second Y value: "))

    slope = ((y2 - y1) / (x2-x1))
    print("The slope of your line is",slope)


#slopeOfLine()

def distanceBetweenPoints():
    x1 = int(input("Please enter your first X value: "))
    y1 = int(input("Please enter your first Y value: "))
    x2 = int(input("Please enter your second X value: "))
    y2 = int(input("Please enter your second Y value: "))

    sqdistance = ((x2 - x1)**2 + (y2-y1)**2)
    distance = math.sqrt(sqdistance)
    print("The distance between your points is",distance)

#distanceBetweenPoints()


def travelStatistics():
    speed = float(input("Please enter the speed of the car in KM/H': "))
    time = float(input("Please enter the length of the journey in hours: "))
    distance = speed * time
    fuel_used = distance / 5
    print("total distance of the journey was",distance,"km")
    print("total fuel used was",fuel_used,"litres")


#travelStatistics()

def sumofSquares():
    uloop = int(input("Please enter the amount of loops that you would like: "))
    listcount = 0
    for i in range(uloop + 1):
        listcount += i ** 2
    print("Sum of Squares:",listcount)

#sumofSquares()



def averageofNumbers():
    list =[]
    loopcount = int(input("Please enter the amount of numbers you would like to average:"))
    for i in range(loopcount):
        inputs= float(input("please enter a number: "))
        list.append(inputs)
    average = sum(list)
    print(average/loopcount)


#averageofNumbers()



def fibonacci():
    n = int(input("Please enter the nth term you're looking for: "))
    n1 = 1
    n2 = 1
    count = 0
    for i in range(n):
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count =+  1
    #print(nth)


#fibonacci()




'''
def selectcoins():
    ''' 1p
        2P
        5p
        10p
        20p
        50p
        £1
        £2
        '''
    pence = int(input("Please enter the amount of Pennies you have: "))
    po2 = pence // 200
    print(po2, "x £2")
    pence = pence - 200
    po1 =pence // 100
    
selectcoins()


'''

















