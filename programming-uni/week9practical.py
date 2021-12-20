#PROMPT FOR ODOMETER (MILEAGE)
#LEGS

#START OF EACH LEG , USER INPUTS THE MILEAGE READING, PETROL USED IN GALLONS. (SEPERATE LINES)

#SIGNALS END OF TRIP WITH A BLANK

#PROGRAM DISPLAYS MPG ON EACH LEG AS INPUTTED
#MPG FOR THE ENTIRE VALUE


#MODIFY INPUT SO IT DOESN'T CRASH IF NOT POSITIVE INTEGETER


totalOdo = 0
totalPetrol = 0
startingOdometer = int(input("Please enter the starting Mileage: "))
while True:
    currentOdometer = input("Please enter the end of leg Mileage reading: ")

    if currentOdometer == "":
        totalMPG = totalOdo /totalPetrol
        print(totalMPG)
        break
    elif currentOdometer.isdigit():
        currentOdometer = int(currentOdometer)
        odometerDiff = currentOdometer - startingOdometer
        startingOdometer = startingOdometer + odometerDiff
        totalOdo = odometerDiff + totalOdo
        #print(odometerDiff)
        #print(startingOdometer)

    petrolUsed = input("Please enter the amount of petrol used in Gallons: ")

    if not petrolUsed.isdigit():
        True
    if petrolUsed.isdigit():
        petrolUsed = int(petrolUsed)
        mPG = odometerDiff /petrolUsed
        totalPetrol += petrolUsed
        print(totalOdo)
        print(mPG)



