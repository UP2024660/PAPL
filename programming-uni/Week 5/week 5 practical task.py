def averageMarksTable():
    file1 = open("marks.txt",'r')
    file1 = file1.read()
    file1.close()
    for item in file1():
        print(item)


averageMarksTable()