
import sys
#import numpy as np
inf = 9999999
def bfs():
	global pair_u, pair_v, dist
	queue = []
	for u in range(1,T+1):
		if pair_u[u] == 0:
			queue.append(u)
			dist[u] = 0
		else:
			dist[u] = inf
	dist[0] = inf
	while len(queue) > 0:
		u = queue.pop(0)
		if dist[u] < inf:

			for v in neighbours[u]:
				if dist[pair_v[v]] == inf:# if v is not paired then pair_v[v] = 0
					# v is not still paired or paired with u 
					# which has other options which still not paired 
					dist[pair_v[v]] = dist[u]+1
					queue.append(pair_v[v])
	return dist[0] != inf

def dfs(u):
	global pair_u, pair_v, dist
	if u != 0:
			for v in neighbours[u]:
				if dist[u]+1 == dist[pair_v[v]]:
					if dfs(pair_v[v]) == True:#pair_v[v] can be zero
						pair_u[u] = v
						pair_v[v] = u
						return True
			dist[u] = inf
			return False
	else:
		return True


def hofcroft():
	global pair_u, pair_v, dist
	pair_u = [0 for j in range(T+1)]
	pair_v = [0 for j in range(H+1)]
	dist = [inf for i in range(1+T+H)]

	matching = 0
	while bfs() == True:
		
		for u in range(1,T+1):
			if pair_u[u] == 0:
				if dfs(u) == True:
		
					matching+=1
	return matching

pair_v = []
pair_u = []
dist = []
if __name__ =='__main__':
	
	f = open('i3.txt','r+') 
	sys.stdin = f 
	
	
	#f = f.read().splitlines()
	[T, H] = [ int(i) for i in sys.stdin.readline().rstrip('\n').split() ]
	neighbours = {}
	neighbours[0]=[]
	

	hotels_visited = [False for i in range(H+1)]
	for h in range(1,T+1):
		neighbours[h] = []
	for t in range(1,T+1):
		hotels = [ int(i) for i in sys.stdin.readline().rstrip('\n').split() ]
		neighbours[t] = []
		for each_hotel in hotels[1:]:
			neighbours[t].append(each_hotel)
			#neighbours[T+each_hotel].append(t)
	#sys.stdin = sys.__stdin__	
	#print(neighbours)
	
	#print(H)
	#print(bandwidth[4])
	#print(bandwidth)

	print(H - hofcroft())
	#print(bandwidth)
