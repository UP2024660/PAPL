def changeCounter():
    inp1 = int(input(" How many 1p coins do you have?: "))
    inp2 = int(input("How many 2p coins do you have?: "))
    inp5 = int(input("How many 5p coins do you have?: "))
    oneP = (1 * inp1)
    twoP = (2 * inp2)
    fiveP = (5 * inp5)
    together= (OneP + TwoP + FiveP)
    print("You have ",Together, "pence")


#changeCounter()

def countTo ():
    inp1= int(input("Please enter a number here: "))
    for i in range (1, inp1+1):
        print(i)
#countTo()



def euros2pounds():
    euro=float(input("Please enter an amount of Euros here: "))
    P = (euro / 1.1)
    Pounds = P
    print("That is ",Pounds, "pounds")


#euros2pounds()
             
def futureValue():
    amount = int(input('Whats the amount '))
    years = int(input('How many years? '))
    for i in range(years):
        amount = amount * 1.055
    print(round(amount))


#futureValue()

def sayHello2():
    print("Hello")
    print("World")

#sayHello2()

def sayName():
    print("Mark Voss")


#sayName()

def sumDifference():
    inp1=int(input("Please enter a big number here: "))
    inp2 =int(input("Please enter a smaller number here: "))
    sum1 = (inp1 + inp2 )
    print(sum1)
    diff = int(inp1 - inp2)
    print(diff)


#sumDifference()


def TenHellos():
    for i in range (0,10):
        print("helllo, world!")

#TenHellos()


def weightsTable():
    print( ' - - - - - - - - - - - - - - - - - - - - - - - '
              ' | 0                     |       0                 | '
              ' | 10                   |       22               | '
              ' | 20                   |       44               | '
              ' | 30                   |       66               | '
              ' | 40                   |       88               | '
              ' | 50                   |       110             | '
              ' | 60                   |       132             | '
              ' | 70                   |       154             | '
              ' | 80                   |       176             | '
              ' | 90                   |       198             | '
              ' | 100                 |      220              | ')


#weightsTable()

def zoomZoom():
    inp1 = int(input("Please enter a number: "))
    for i in range(1, inp1+1):
        print("Zoom",i)

#zoomZoom()





