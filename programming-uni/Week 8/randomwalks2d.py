def distanceAway(x, y):
    return (abs(x)**2 + abs (y))**0.5

def main():
    numWalks, numSteps = getInputs()
    averageSteps = takeWalks(numWalks, numSteps)
    printExpectedDistance(averageSteps)

def getInputs():
    numWalks = int(input("How many random walks to take? "))
    numSteps = int(input("How many steps for each walk? "))
    return numWalks, numSteps

def takeWalks(numWalks, numSteps):
    totalSteps = 0
    for walk in range(numWalks):
        stepsAway = takeAWalk(numSteps)
        totalSteps += stepsAway
    return totalSteps / numWalks

def printExpectedDistance(averageSteps):
    print("The expected number of steps away from the", end=" ")
    print(f"start point is, {averageSteps:.5f}")


def takeAWalk(numSteps):
    from random import random
    stepsForwardOfStartX = 0
    stepsForwardOfStartY = 0
    for step in range(numSteps):
        if random() < 0.5:
            if random() < 0.5:
                stepsForwardOfStartX -= 1
            else:
                stepsForwardOfStartX =  step
        else:
            if random() <0.5:
                stepsForwardOfStartY -= 1
            else:
                stepsForwardOfStartY = step

    return distanceAway(stepsForwardOfStartX, stepsForwardOfStartY)


main()