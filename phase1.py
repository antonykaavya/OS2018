# Kaavya Antony
# Nate Brown
# Patrick Davis
# Austin DiMartino
# Ousmane Dieng

import queue # storing the processes
import csv # reading into data
import pandas as pd # data processing

class Process(object):
    def __init__(self, priority=100, ID=0, owner="", memory=0):
    	self.priority = priority
    	self.owner = owner 
    	self.ID = ID    	
    	self.memory = memory 
        
    def __cmp__(self, other):
        return cmp(self.priority, other.priority)
  
def main():
	df = pd.read_csv("/Users/Kaavya/Documents/OS/OS2018/processes.csv")

	ids = df["ID"]
	priorities = df["priority"]
	owners = df["owner"]
	memory = df["memory_required"]

	valid_ids = []
	for i in range(len(ids)):
		try:
			valid_ids.append(int(ids[i]))
		except: 
			valid_ids.append(str(ids[i]))
	#print(valid_ids)
	 
	valid_priority = []
	for i in range(len(priorities)):
		try:
			valid_priority.append(int(priorities[i]))
		except:
			# print("Priority = 0")
			valid_priority.append(100)
	#print(valid_priority)

	valid_owners = []
	for i in range(len(owners)):
		try:
			valid_owners.append(int(owners[i]))
		except: 
			valid_owners.append(str(owners[i]))
	#print(valid_owners)

	valid_memory = []
	for i in range(len(memory)):
		try:
			valid_memory.append(int(memory[i]))
		except:
			# print("Priority = 0")
			valid_memory.append(0)
	#print(valid_memory)

	L = queue.PriorityQueue()

	for i in range(len(valid_ids)):
		#process1 = Process(valid_priority[i], valid_ids[i], valid_owners[i], valid_memory[i])
		L.put((valid_priority[i], valid_ids[i], valid_owners[i], valid_memory[i])) 

	while not L.empty():
		process = L.get()
		print ('Process:', process)

	print("Here is what the order of the priority queue should be: 2, 3, 8, 17, 100")

main()
