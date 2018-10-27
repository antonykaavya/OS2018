# Kaavya Antony
# Nate Brown
# Patrick Davis
# Austin DiMartino
# Ousmane Dieng

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
    with open('newprocesses.csv','a') as newfile:
        writer=csv.writer(newfile)
        with open('newprocesses.csv','r') as csvfile:
            writer.writerow(process)
                
def main():
    # create graphical window
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

    #get user input for process priority
    priorityText = Text(Point(500, 275), "Input priority (between 1 and 100): ")
    priorityText.draw(win)    
    priorityInput = Entry(Point(500, 300), 20)
    priorityInput.draw(win)

    #get user input for process owner
    ownerText = Text(Point(700, 275), "Input owner (a string): ")
    ownerText.draw(win)    
    ownerInput = Entry(Point(700, 300), 20)
    ownerInput.draw(win)

    #get user input for process memory
    memoryText = Text(Point(900, 275), "Input memory (between 100 and 1000): ")
    memoryText.draw(win)    
    memoryInput = Entry(Point(900, 300), 20)
    memoryInput.draw(win)

    pt = win.getMouse()

    # While the exit button is not clicked
    while not (600 <= pt.getX() <= 800 and 400 <= pt.getY() <= 450):

	# if the add new process button is clicked
        if (350 <= pt.getX() <=550 and 400 <= pt.getY() <= 450):
            # creates a priority queue L that will store the processes            
            L = queue.PriorityQueue()
            # get the text from all the input boxes
            ids = idInput.getText()
            priorities = priorityInput.getText()
            owners = ownerInput.getText()
            memory = memoryInput.getText()
            error = Text(Point(600, 100), "")
            error.draw(win)

            i = 0
            # ensure that the ID is valid
            try:
                ids = int(ids)
                i += 1
            except: 
                error.setText("ID was not an integer, try again!")

            # ensure that the priority is valid
            try: 
                priorities = int(priorities)                
                if (1 <= priorities <= 100):
                    i += 1
            except: 
                error.setText("Priority was not between 1 and 100, try again!")

            # ensure that the owner is valid
            try:
                owners = int(owners)
                error.setText("Owner was not a string, try again!")
            except: 
                i += 0

            # ensure that the memory is valid
            try:                     
                memory = int(memory)
                if (100 <= memory <= 1000):
                    i += 1
            except: 
                error.setText("Memory was not between 100 and 1000, try again!")

            # if all the parameters are valid, add the process to the queue
            if i == 4:
                L.put((ids, priorities, owners, memory))
                process = L.get()
                addProcesstoFile(process)
                # print the process
                print ('Process:', process)

            # reset the input boxes so that more processes can be added
            priorityInput.setText("")
            idInput.setText("")
            ownerInput.setText("")
            memoryInput.setText("")
        
        pt = win.getMouse()
        
    win.close()

main()
