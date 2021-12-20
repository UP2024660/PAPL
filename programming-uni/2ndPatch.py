from graphics import *

def drawPatch(win,x,y,colour):
    #win = GraphWin()
    x0 = x
    y0 = y
    x1 = x + 100
    y1 = y + 100
    for i in range(0,100,10):
        drawLine(win,Point(x0+i,y0), Point(x1-i,y1),colour)
        drawLine(win,Point(x0,y0+i), Point(x1,y1-i),colour)

def drawLine(win,p1,p2,colour):
        line = Line(p1, p2)
        line.setFill(colour)
        line.setOutline(colour)
        line.draw(win)



def drawRectangle(win,p1,p2,colour):
    rectangle = Rectangle(Point(0,0),Point(5,20))
    rectangle.setFill(colour)
    rectangle.draw(win)
    rectangle = Rectangle(Point(5,0),Point(10,20))
    rectangle.setFill("white")
    rectangle.draw(win)
    rectangle = Rectangle(Point(10,0),Point(15,20))
    rectangle.setFill(colour)
    rectangle.draw(win)
    rectangle = Rectangle(Point(15,0),Point(20,20))
    rectangle.setFill("white")
    rectangle.draw(win)

    rectangle = Rectangle(Point(40,0),Point(45,20))
    rectangle.setFill(colour)
    rectangle.draw(win)
    rectangle = Rectangle(Point(45,0),Point(50,20))
    rectangle.setFill("white")
    rectangle.draw(win)
    rectangle = Rectangle(Point(50,0),Point(55,20))
    rectangle.setFill(colour)
    rectangle.draw(win)
    rectangle = Rectangle(Point(55,0),Point(60,20))
    rectangle.setFill("white")
    rectangle.draw(win)


    rectangle = Rectangle(Point(80,0),Point(85,20))
    rectangle.setFill(colour)
    rectangle.draw(win)
    rectangle = Rectangle(Point(85,0),Point(90,20))
    rectangle.setFill("white")
    rectangle.draw(win)
    rectangle = Rectangle(Point(90,0),Point(95,20))
    rectangle.setFill(colour)
    rectangle.draw(win)
    rectangle = Rectangle(Point(95,0),Point(100,20))
    rectangle.setFill("white")
    rectangle.draw(win)

# horizontals
    rectangle = Rectangle(Point(20,0),Point(40,5))
    rectangle.setFill(colour)
    rectangle.draw(win)
    rectangle = Rectangle(Point(20,5),Point(40,10))
    rectangle.setFill("white")
    rectangle.draw(win)
    rectangle = Rectangle(Point(20,10),Point(40,15))
    rectangle.setFill(colour)
    rectangle.draw(win)
    rectangle = Rectangle(Point(20,15),Point(40,20))
    rectangle.setFill("white")
    rectangle.draw(win)


    rectangle = Rectangle(Point(60,0),Point(80,5))
    rectangle.setFill(colour)
    rectangle.draw(win)
    rectangle = Rectangle(Point(60,5),Point(80,10))
    rectangle.setFill("white")
    rectangle.draw(win)
    rectangle = Rectangle(Point(60,10),Point(80,15))
    rectangle.setFill(colour)
    rectangle.draw(win)
    rectangle = Rectangle(Point(60,15),Point(80,20))
    rectangle.setFill("white")
    rectangle.draw(win)


    rectangle = Rectangle(Point(20,40),Point(40,45))
    rectangle.setFill(colour)
    rectangle.draw(win)
    rectangle = Rectangle(Point(20,45),Point(40,50))
    rectangle.setFill("white")
    rectangle.draw(win)
    rectangle = Rectangle(Point(20,50),Point(40,55))
    rectangle.setFill(colour)
    rectangle.draw(win)
    rectangle = Rectangle(Point(20,55),Point(40,60))
    rectangle.setFill("white")
    rectangle.draw(win)


    rectangle = Rectangle(Point(60,40),Point(80,45))
    rectangle.setFill(colour)
    rectangle.draw(win)
    rectangle = Rectangle(Point(60,45),Point(80,50))
    rectangle.setFill("white")
    rectangle.draw(win)
    rectangle = Rectangle(Point(60,50),Point(80,55))
    rectangle.setFill(colour)
    rectangle.draw(win)
    rectangle = Rectangle(Point(60,55),Point(80,60))
    rectangle.setFill("white")
    rectangle.draw(win)


    rectangle = Rectangle(Point(20,80),Point(40,85))
    rectangle.setFill(colour)
    rectangle.draw(win)
    rectangle = Rectangle(Point(20,85),Point(40,90))
    rectangle.setFill("white")
    rectangle.draw(win)
    rectangle = Rectangle(Point(20,90),Point(40,95))
    rectangle.setFill(colour)
    rectangle.draw(win)
    rectangle = Rectangle(Point(20,95),Point(40,100))
    rectangle.setFill("white")
    rectangle.draw(win)


    rectangle = Rectangle(Point(60,80),Point(80,85))
    rectangle.setFill(colour)
    rectangle.draw(win)
    rectangle = Rectangle(Point(60,85),Point(80,90))
    rectangle.setFill("white")
    rectangle.draw(win)
    rectangle = Rectangle(Point(60,90),Point(80,95))
    rectangle.setFill(colour)
    rectangle.draw(win)
    rectangle = Rectangle(Point(60,95),Point(80,100))
    rectangle.setFill("white")
    rectangle.draw(win)





    #third row
    rectangle = Rectangle(Point(0,40),Point(5,60))
    rectangle.setFill(colour)
    rectangle.draw(win)
    rectangle = Rectangle(Point(5,40),Point(10,60))
    rectangle.setFill("white")
    rectangle.draw(win)
    rectangle = Rectangle(Point(10,40),Point(15,60))
    rectangle.setFill(colour)
    rectangle.draw(win)
    rectangle = Rectangle(Point(15,40),Point(20,60))
    rectangle.setFill("white")
    rectangle.draw(win)




    rectangle = Rectangle(Point(40,40),Point(45,60))
    rectangle.setFill(colour)
    rectangle.draw(win)
    rectangle = Rectangle(Point(45,40),Point(50,60))
    rectangle.setFill("white")
    rectangle.draw(win)
    rectangle = Rectangle(Point(50,40),Point(55,60))
    rectangle.setFill(colour)
    rectangle.draw(win)
    rectangle = Rectangle(Point(55,40),Point(60,60))
    rectangle.setFill("white")
    rectangle.draw(win)


    rectangle = Rectangle(Point(80,40),Point(85,60))
    rectangle.setFill(colour)
    rectangle.draw(win)
    rectangle = Rectangle(Point(85,40),Point(90,60))
    rectangle.setFill("white")
    rectangle.draw(win)
    rectangle = Rectangle(Point(90,40),Point(95,60))
    rectangle.setFill(colour)
    rectangle.draw(win)
    rectangle = Rectangle(Point(95,40),Point(100,60))
    rectangle.setFill("white")
    rectangle.draw(win)

    #final row

    rectangle = Rectangle(Point(0,80),Point(5,100))
    rectangle.setFill(colour)
    rectangle.draw(win)
    rectangle = Rectangle(Point(5,80),Point(10,100))
    rectangle.setFill("white")
    rectangle.draw(win)
    rectangle = Rectangle(Point(10,80),Point(15,100))
    rectangle.setFill(colour)
    rectangle.draw(win)
    rectangle = Rectangle(Point(15,80),Point(20,100))
    rectangle.setFill("white")
    rectangle.draw(win)



#horizontals
    rectangle = Rectangle(Point(40,80),Point(45,100))
    rectangle.setFill(colour)
    rectangle.draw(win)
    rectangle = Rectangle(Point(45,80),Point(50,100))
    rectangle.setFill("white")
    rectangle.draw(win)
    rectangle = Rectangle(Point(50,80),Point(55,100))
    rectangle.setFill(colour)
    rectangle.draw(win)
    rectangle = Rectangle(Point(55,80),Point(60,100))
    rectangle.setFill("white")
    rectangle.draw(win)


    rectangle = Rectangle(Point(80,80),Point(85,100))
    rectangle.setFill(colour)
    rectangle.draw(win)
    rectangle = Rectangle(Point(85,80),Point(90,100))
    rectangle.setFill("white")
    rectangle.draw(win)
    rectangle = Rectangle(Point(90,80),Point(95,100))
    rectangle.setFill(colour)
    rectangle.draw(win)
    rectangle = Rectangle(Point(95,80),Point(100,100))
    rectangle.setFill("white")
    rectangle.draw(win)

#third























#def drawRectangle():

 #   height = int(input("Please enter the height: "))
  #  width = int(input("Please enter the width: "))
 #   win = GraphWin("Rectangle")
 # #  topleftx = 100 - (width / 2 )
 #   toplefty = 100 + (height /  2)
  #  botrightx = 100 + (width / 2)
  ##  botrighty = 100 - (height / 2)
  #  rectangle = Rectangle(Point(topleftx,toplefty), Point(botrightx, botrighty))
 #   rectangle.draw(win)
 #   win.getMouse()
  #  win.close()





def drawPatchwork():
    win = GraphWin("Patchwork", 100,100, autoflush = False)
    x =0
    y = 20
    for i in range(3):
        for j in range(3):
            drawRectangle(win,x,y,"red")
            x += 20
        x = (0)
        y = y + 20
    #drawRectangle(win,x,y,"red")

    win.getMouse()
    win.close()



