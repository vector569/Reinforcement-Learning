import numpy as np
import grid
import math

def ret_max(array):
    max_ = -9999999999999999
    index = 0
    for i in range(len(array)):
        if array[i] > max_:
            max_= array[i]
            index = i
    indices=[]        
    for i in range(len(array)):
        if array[index] == array[i]:
            indices.append(i)
    f_index = indices[np.random.random_integers(0,len(indices)-1)]
    return [max_,f_index]

def action(state,V,u,n_episodes,epsilon=0.2):
	epsilon *= 1 - u/n_episodes
	action_set = world[state][1]
	Q = []
	for i in action_set:
		Q.append(V[obj.new_state(state,i)])
	temp1 = np.random.choice(2, 1, p=[epsilon,1-epsilon])
	#Exploit
	if temp1 == 1:
		action = ret_max(Q)[1]
	#Explore
	else:
		action = np.random.random_integers(0,len(action_set)-1)
	return action_set[action]


# nXn, range_reward/range_noise = 5
n = 5
obj = grid.Gridworld(n,5)
[world,values] = obj.world()

# TD[0]
# Declaring initial values and policy
V = []
for i in range(n*n):
	V.append(0)

n_episodes = 1000
all_trails = []
alpha = 0.01
gamma = 0.8
epsilon = 0.05
for u in range(n_episodes):
	s = obj.start_state
	trail = [s]
	while(s != obj.terminal_state):
		#A <- action from pi and s through softmax
		a = action(s,V,u,n_episodes,epsilon)
		[s_p,R] = obj.take_action(s,a)
		V[s] = V[s] + alpha*(1-u/n_episodes)*(R + gamma*V[s_p] - V[s])
		s = s_p
		trail.append(s)
	all_trails.append(trail)
	print(u+1)
print(all_trails[n_episodes-1])
print(V)
print(values)
