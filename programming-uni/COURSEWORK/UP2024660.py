from graphics import *
validColours= ["red","green","blue","magenta","orange","cyan"] # list of Valid colours

def main():
    cont = True
    userColour = [] #List of Input-ed colours
    while len(userColour) < 3: # while the length of the list is less than 3, enter a colour
        col = input("Please enter a colour here: ")
        col = col.lower() # makes the input lowercase
        if col not in validColours:
            print("These are acceptable colours : red,green,blue,magenta,orange,cyan")
        elif userColour.count(col) == 2:
            print("Not allowed more than two of the same colour")
        else:
            userColour.append(col)
            cont = True


    sizeloop = True
    while sizeloop:
        size = int(input("Please enter size 5 for 5x5 or 7 for 7x7: "))
        if size == 5 or size ==7:
            sizeloop = False

    win = GraphWin("Patchwork", 100*size ,100*size, autoflush = False) # this draws the window to the same size as the inputted size
    colour0 = userColour[0]
    colour1 = userColour[1]
    colour2 = userColour[2]

    drawTotalWindow(win,size,colour0,colour1,colour2)

    win.getMouse()
    win.close()


def drawTotalWindow(win,size,colour0,colour1,colour2): #This draws the Patch to the full size of the window
    for x in range(0,size*100,100): #for x in range 5/7
        y = size*100 # Y value goes down, making the columns of patterns
        for j in range(0,size*100,100):
            y = y - 100
            if x < j and x < y:
                drawSecondPatch(win,x,j,colour1) # this draws the left side of the pattern, based on the boundar set between x<j and x<y
            elif x > j and x > y:
                drawSecondPatch(win,x,j,colour2) # ^ but the right side
            else:
                drawFinalPatch(win,x,j,colour0) # fills in the rest outside of the two boundaries

def drawFinalPatch(win,x,y,colour0):
    x = x
    y = y
    x1 = x + 100
    y1 = y + 100
    for i in range(0,100,10):
        drawLine(win,Point(x+i,y), Point(x1-i,y1),colour0) # this draws the lines along the top and bottom
        drawLine(win,Point(x,y+i), Point(x1,y1-i),colour0)  # this draws them on the right and left
        drawLine(win,Point(x,y1),Point(x1,y),colour0)



def drawLine(win,p1,p2,colour0):#This abstracts the linedrawing to one function
        line = Line(p1, p2)
        line.setOutline(colour0)
        line.draw(win)



def drawSecondPatch(win,x2,y2,colour1):
    topRightXValue = 5 # the value of the right most point of each small rectangle
    yValue = 20 # the y Val of the lowest point of each rectangle
    changeColour = True
    rectangleOrientation = True
    for row in range(5): # this draws the columns
        x = x2
        for column in range(5):
            x = x2 + (20 * (column)) # this draws each pattern along the x axis 5 times , and then another 5 times based on the row loop
            y = y2 + (20 * (row))
            for j in range(4):
                if changeColour:
                    colour = colour1 # colour is the userInput colour from the main function
                else:
                    colour = "white"

                if rectangleOrientation: # this draws each small square of rectangles , either vertically (in this case) or horizontally (else)
                    topRightXValue = 5
                    yValue = 20
                    drawRectangle(win,colour,x,y,topRightXValue,yValue)

                    changeColour = not changeColour # flips the colour of each rectangle , as in RED/WHITE/RED/WHITE for example
                    x +=5

                else:
                    topRightXValue = 20
                    yValue = 5
                    drawRectangle(win,colour,x,y,topRightXValue,yValue)

                    y +=5
                    changeColour = not changeColour

            rectangleOrientation = not rectangleOrientation # flips the orientation VERTICAL/HORIZONTAL/VERTICAL/HORIZONTAL/VERTICAL
        changeColour = not changeColour


def drawRectangle(win,colour,x,y,topRightXValue,yValue):# This function breaks down the rectangle drawing part of the second patch into one function
    rectangle = Rectangle(Point(x,y),Point(x+topRightXValue,y+yValue))
    rectangle.setFill(colour)
    rectangle.draw(win)


main()
