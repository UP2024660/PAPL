#Week 9 : P8
#Coin Flips

from random import *



def getInputs():
    numFlips = int(input("How many times would you like to flip the coin? "))
    return numFlips


def simulateFlips(numFlips):
    heads = randint(0,numFlips)
    tails = numFlips - heads

    headsProportion = heads/numFlips
    tailsProportion = tails/numFlips

    return (headsProportion, tailsProportion)




def displayResults(headsProportion,tailsProportion):
    print("Heads {:.2f}".format(headsProportion), end = '')
    print(", Tails {:.2f}".format(tailsProportion))

def main():
    numFlips = getInputs()
    headsProportion,tailsProportion = simulateFlips(numFlips)
    displayResults(headsProportion,tailsProportion)


main()