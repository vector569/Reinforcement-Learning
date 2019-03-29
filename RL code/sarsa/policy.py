import numpy as np
import grid
import math

def ret_max(array1):
    max_ = -9999999999999999
    index = 0
    array = []
    for i in range(len(array1)):
    	array.append(array1[i][1])
    for i in range(len(array)):
        if array[i] > max_:
            max_= array[i]
            index = i
    indices=[]        
    for i in range(len(array)):
        if array[index] == array[i]:
            indices.append(i)
    f_index = indices[np.random.random_integers(0,len(indices)-1)]
    return array1[f_index][0]

def action(state,Q,u,n_episodes,epsilon=0.2):
	action_set = world[state][1]
	epsilon *= (1-u/n_episodes)
	val = []
	for i in range(len(Q)):
		if Q[i][0] == state:
			val.append([Q[i][1],Q[i][2]])
	temp1 = np.random.choice(2, 1, p=[epsilon,1-epsilon])
	#Exploit
	if temp1 == 1:
		action = ret_max(val)
		return action
	#Explore
	else:
		action = np.random.random_integers(0,len(val)-1)
		return val[action][0]


# nXn, range_reward/range_noise = 5
n = 3
obj = grid.Gridworld(n,5)
[world,values] = obj.world()

# SARSA
# Declaring initial values and policy
# len(Q) = 4n(n-1)
V = []
Q = []
for i in range(n*n):
	V.append(0)
	action_set = world[i][1]
	for j in action_set:
		Q.append([i,j,0])

n_episodes = 1000
all_trails = []
alpha = 0.01
gamma = 0.8
epsilon = 0.05
for u in range(n_episodes):
	s = obj.start_state
	a = action(s,Q,u,n_episodes,epsilon)
	trail = [s]
	while(s != obj.terminal_state):
		[s_p,R] = obj.take_action(s,a)
		a_p = action(s_p,Q,u,n_episodes,epsilon)

		action_seti = world[s][1]
		action_setj = world[s_p][1]
		for i in range(len(Q)):
			for j in range(len(Q)):
				if Q[i][0] == s and Q[i][1] == a and Q[j][0] == s_p and Q[j][1] == a_p:
					Q[i][2] = Q[i][2] + alpha*(1-u/n_episodes)*(R + gamma*Q[j][2] - Q[i][2])
		s = s_p
		a = a_p
		trail.append(s)
	all_trails.append(trail)
	print(u+1)
print(all_trails[n_episodes-1])
print(Q)
print(values)