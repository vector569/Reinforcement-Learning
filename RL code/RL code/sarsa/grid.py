import numpy as np
import matplotlib.pyplot as plt
# n >= 3
# Array of [State,Value,Actions] for i in 0 to n*2-1
class Gridworld:
	def __init__(self,*args):
		n = args[0]
		std = args[1]
		self.n = n
		self.grid = []
		self.start_state = 0
		self.terminal_state = n*n-1
		for i in range(n*n):
			self.grid.append([i,-1,self.transitions(i)])
			#if i%2 == 0:
			#	self.grid.append([i,-n*n-1,self.transitions(i)])
			#else:
			#	self.grid.append([i,i,self.transitions(i)])
				#self.grid.append([i,(np.random.random(1)[0]-0.5)*2*std,self.transitions(i)])

            
	def classification(self,state):
		x = self.n
		cat = ""
		if state == 0:
			cat = "BLC" #Bottom left corner
		elif state == x-1:
			cat = "BRC" #Bottom right corner
		elif state == (x*x-x):
			cat = "TLC" #Top left corner
		elif state == (x*x-1):
			cat = "TRC" #Top right corner
		elif 0<state and state<x-1:
			cat = "BE" #Bottom edge
		elif (x*x-x)<state and state<(x*x-1):
			cat = "TE" #Top edge
		elif (state+1)%x == 0 and 1<(state+1)/x and (state+1)/x<x:
			cat = "RE" #Right edge
		elif state%x == 0 and 0<(state/x) and (state/x)<(x-1):
			cat = "LE" #Left edge
		else:
			cat = "M" #Middle
		return cat
            
	def transitions(self,state):
		cat = self.classification(state)
		if cat == "M":
			actions = ["T","R","B","L"]
		elif cat == "LE":
			actions = ["T","R","B"]
		elif cat == "RE":
			actions = ["T","B","L"]
		elif cat == "TE":
			actions = ["R","B","L"]
		elif cat == "BE":
			actions = ["T","R","L"]
		elif cat == "BLC":
			actions = ["T","R"]
		elif cat == "BRC":
			actions = ["T","L"]
		elif cat == "TLC":
			actions = ["R","B"]
		elif cat == "TRC":
			actions = ["B","L"]
		return actions

	def world(self):
		arr1 = []
		arr2 = []
		for i in self.grid:
			arr1.append([i[0],i[2]])
			arr2.append(i[1])
		return [arr1,arr2]

	def new_state(self,state,action):
		if action == "T":
			return(state + self.n)
		elif action == "B":
			return(state - self.n)
		elif action == "R":
			return(state+1)
		elif action == "L":
			return(state-1)

	def take_action(self,state,action):
		ns = self.new_state(state,action)
		noise = 0 #Default = 2
		reward = self.grid[ns][1] + (np.random.random(1)[0]-0.5)*noise
		return [ns,reward]
