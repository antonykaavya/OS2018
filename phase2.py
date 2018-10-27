# Kaavya Antony
# Nate Brown
# Patrick Davis
# Austin DiMartino
# Ousmane Dieng

### IO freq is how many cycles the process is run before being interrupted, it is interuppted for IO duration = 5 CLOCK CYCLES

import queue # storing the processes
import csv # reading into data
from graphics import*

# creates a Button method used for 
def drawbutton(win, pt1, pt2, words):
    button = Rectangle(pt1,pt2)
    button.setFill("Blue")
    button.draw(win)
    midpointX = (pt2.getX() + pt1.getX())/2
    midpointY = (pt2.getY() + pt1.getY())/2
    buttonLabel = Text(Point(midpointX, midpointY), words)
    buttonLabel.setFill("white")
    buttonLabel.draw(win)

# adds our valid process to the csv file
def addProcesstoFile(process):
    with open('newprocesses2.csv','a') as newfile:
        writer=csv.writer(newfile)
        with open('newprocesses2.csv','r') as csvfile:
            writer.writerow(process)
                
# ensures that the memory inputted by the user is valid
def getMemory(win, memoryInput):
    error = Text(Point(600, 100), "")
    error.draw(win)
    try: 
        memory = int(memoryInput)                
        if (1 <= memory <= 10):
            return memory
    except: 
        error.setText("Memory was not between 1 and 10, try again!")
        return -1

# ensures that the ID inputted by the user is valid
def getID(win, idInput):
    error = Text(Point(600, 100), "")
    error.draw(win)
    try:
        ids = int(idInput)
        return ids
    except: 
        error.setText("ID was not an integer, try again!")
        return -1

# ensures that the arrival time inputted by the user is valid
def getArrivalTime(win, arrivalInput):
    error = Text(Point(600, 100), "")
    error.draw(win)    
    try:                     
        arrival = int(arrivalInput)
        if (1 <= arrival <= 100):
            return arrival 
    except: 
        error.setText("Arrival was not between 1 and 100, try again!")    
        return -1

def main():
    # create graphical window
    win=GraphWin("OS Scheduler", 1200,1000)
    #creates button for Add New Process
    pt1 = Point(350, 400)
    pt2 = Point(550, 450)
    processBox = drawbutton(win, pt1, pt2, "Round Robin")

    #creates button for Exit
    pt3 = Point(600, 400)
    pt4 = Point(800, 450)
    exitBox = drawbutton(win, pt3, pt4, "First Come First Serve")

    #creates button for Exit
    pt3 = Point(850, 400)
    pt4 = Point(1050, 450)
    exitBox = drawbutton(win, pt3, pt4, "Exit")

    while not (850 <= pt.getX() <=1050 and 400 <= pt.getY() <= 450):
        if (350 <= pt.getX() <=550 and 400 <= pt.getY() <= 450):
            print("Round Robin")
            return 1
        elif (600 <= pt.getX() <=800 and 400 <= pt.getY() <= 450):
            print("First Come First Serve")
            return 0
        win.close()

    win=GraphWin("OS Scheduler", 1200,1000)

    #creates button for Add New Process
    pt1 = Point(350, 400)
    pt2 = Point(550, 450)
    processBox = drawbutton(win, pt1, pt2, "Add New Process")

    #creates button for Exit
    pt3 = Point(600, 400)
    pt4 = Point(800, 450)
    exitBox = drawbutton(win, pt3, pt4, "Exit")

    #get user input for process ID
    idText = Text(Point(300, 275), "Input ID (an integer): ")
    idText.draw(win)
    idInput = Entry(Point(300, 300), 20)
    idInput.draw(win)

    #get user input for process memory
    memoryText = Text(Point(500, 275), "Input memory (between 1 and 10): ")
    memoryText.draw(win)    
    memoryInput = Entry(Point(500, 300), 20)
    memoryInput.draw(win)

    #get user input for process arrival
    arrivalText = Text(Point(700, 275), "Input arrival time (between 1 and 100): ")
    arrivalText.draw(win)    
    arrivalInput = Entry(Point(700, 300), 20)
    arrivalInput.draw(win)

    pt = win.getMouse()

    # While the exit button is not clicked
    while not (600 <= pt.getX() <= 800 and 400 <= pt.getY() <= 450):

	# if the add new process button is clicked
        if (350 <= pt.getX() <=550 and 400 <= pt.getY() <= 450):
            # creates a priority queue L that will store the processes            
            L = queue.PriorityQueue()

            i = 0
            if getMemory(win,memoryInput.getText()) != -1:
                i += 1

            if getID(win, idInput.getText()) != 1:
                i += 1

            if getArrivalTime(win, arrivalInput.getText()) != -1:
                i += 1        

            # if all the parameters are valid, add the process to the queue
            if i == 3:
                L.put((idInput.getText(), idInput.getText(), memoryInput.getText()))
                process = L.get()
                # add process to output file
                addProcesstoFile(process)
                # print the process
                print ('Process:', process)

            # reset the input boxes so that more processes can be added
            arrivalInput.setText("")
            idInput.setText("")
            memoryInput.setText("")
        
        pt = win.getMouse()
        
    win.close()

main()
