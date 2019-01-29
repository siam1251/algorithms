
import sys
max_dis = 9999

def get_min_distance(start, prev,total):
	cost = []
	if total >= 3 and distance[start][prev] != max_dis:
		return 0
	
	if table[prev][total] != -1:
		return table[prev][total]
	for l in range(1,locations+1):
		if visited[l] == False:
			if prev != -1:
				if distance[prev][l] != max_dis:
					visited[l] = True
					cost.append( distance[prev][l]+get_min_distance(start,l,total+1))
					table[prev][total] = cost[-1]
					visited[l] = False

			else:
				start = l
				visited[l] = True
				cost.append(get_min_distance(start,l,total+1))
				#table[prev][total] = cost[-1]
				visited[l] = False
	if len(cost) >= 1:
		return min(cost)
	else: 
		return max_dis

if __name__ == '__main__':
	f = open('i2.txt','r')
	sys.stdin = f  
	#f = f.read().splitlines()
	T = int(input())
	for t in range(T):
		[locations, roads] = [ int(i) for i in input().split() ]
		table = [[ -1 for j in range(locations+1)]for i in range(locations+1)]
		#print(table)
		distance = [ [max_dis for i in range(locations+1)] for i in range(locations+1)]
		visited = [False for i in range(locations+1)]
		for e in range(roads):
			values =[ int(i) for i in input().split() ]
			#print(values)
			distance[values[0]][values[1]] = values[2]
			distance[values[1]][values[0]] = values[2]
		print(get_min_distance(-1,-1, 0))
		#print('-------------------------------------')
		