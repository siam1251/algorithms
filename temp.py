
import sys
max_dis = 9999

def get_min_distance(prev,total):
	cost = []
	
	

	for l in range(1,locations+1):
		if visited[l] == False:
			if prev != -1:
				if distance[prev][l] != max_dis:
					visited[l] = True
					cost.append(distance[prev][l]+get_min_distance(l,total+1))
					visited[l] = False

			else:
				visited[l] = True
				cost.append(get_min_distance(l,total+1))
				visited[l] = False
	if len(cost) >= 1:
		return min(cost)
	else: 
		return 0

if __name__ == '__main__':
	f = open('i2.txt','r')
	sys.stdin = f  
	#f = f.read().splitlines()
	T = int(input())
	for t in range(T):
		[locations, roads] = [ int(i) for i in input().split() ]
		distance = [ [max_dis for i in range(locations+1)] for i in range(locations+1)]
		visited = [False for i in range(locations+1)]
		for e in range(roads):
			values =[ int(i) for i in input().split() ]
			#print(values)
			distance[values[0]][values[1]] = values[2]
			distance[values[1]][values[0]] = values[2]
		print(get_min_distance(-1, 0))
		
		