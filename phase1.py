# Kaavya Antony
# Nate Brown
# Patrick Davis
# Austin DiMartino
# Ousmane Dieng

import queue # storing the processes
import csv # reading into data
import pandas as pd # data processing

# create a Process class with parameters priority (int), ID (string or int), owner (string), and memory (int)
class Process(object):
    def __init__(self, priority=100, ID=0, owner="", memory=0):
    	self.priority = priority
    	self.owner = owner 
    	self.ID = ID    	
    	self.memory = memory 
        
    def __cmp__(self, other):
        return cmp(self.priority, other.priority)
  
def main():
	# reads in CSV file with the processes
	df = pd.read_csv("/Users/Kaavya/Documents/OS/OS2018/processes.csv")

	# gets columns of each processes' parameters
	ids = df["ID"]
	priorities = df["priority"]
	owners = df["owner"]
	memory = df["memory_required"]

	# checks to see if the IDs are valid (either int or string)
	valid_ids = []
	for i in range(len(ids)):
		try:
			valid_ids.append(int(ids[i]))
		except: 
			valid_ids.append(str(ids[i]))
	#print(valid_ids)
	 
	# checks to see if the priorities are valid (either a valid int or we make the priority 100 to give the process a low priority)
	valid_priority = []
	for i in range(len(priorities)):
		try:
			valid_priority.append(int(priorities[i]))
		except:
			# print("Priority = 0")
			valid_priority.append(100)
	#print(valid_priority)

	# checks to see if the owners are valid 
	valid_owners = []
	for i in range(len(owners)):
		try:
			valid_owners.append(int(owners[i]))
		except: 
			valid_owners.append(str(owners[i]))
	#print(valid_owners)

	# checks to see if the memory is valid, if not we make the memory 0
	valid_memory = []
	for i in range(len(memory)):
		try:
			valid_memory.append(int(memory[i]))
		except:
			# print("Priority = 0")
			valid_memory.append(0)
	#print(valid_memory)

	# creates a priority queue L that will store the processes
	L = queue.PriorityQueue()

	# if the processes are valid, add them to the queue
	for i in range(len(valid_ids)):
		#process1 = Process(valid_priority[i], valid_ids[i], valid_owners[i], valid_memory[i])
		L.put((valid_priority[i], valid_ids[i], valid_owners[i], valid_memory[i])) 

	# print all the processes
	while not L.empty():
		process = L.get()
		print ('Process:', process)

	print("Here is what the order of the priority queue should be: 2, 3, 8, 17, 100")

main()
