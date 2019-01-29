def find_a_path(current):
	#print(current)
	global bandwidth
	global sink
	if hotels_visited[current] == False:
		#print('--------')
		hotels_visited[current] = True
		return True
	no_neighbour = True
	
	for neighbour in neighbours[current]:
		# print(neighbours[current])
		# print(neighbour)
		if bandwidth[current][neighbour] > 0 and visited[neighbour] == False:
			no_neighbour = False
			last = True
			bandwidth[current][neighbour] -= 1
			bandwidth[neighbour][current] += 1
			visited[neighbour] = True
			path_exist = find_a_path(neighbour)
			visited[neighbour] = False
			if path_exist == False:# reseting the bandwidth
				bandwidth[current][neighbour] += 1
				bandwidth[neighbour][current] -= 1
				last = False
			elif path_exist == True: return True
	if no_neighbour == True:
		return False


def max_flow():
	path_exist = True
	free_visits = 0
	for t in range(1,T+1):
		rt = find_a_path(t)
		if rt == True:
			free_visits += 1
		
	return free_visits
import sys
if __name__ =='__main__':
	
	f = open('i3.txt','r+') 
	sys.stdin = f 
	
	
	#f = f.read().splitlines()
	[T, H] = [ int(i) for i in sys.stdin.readline().rstrip('\n').split() ]
	neighbours = {}
	neighbours[0]=[]
	bandwidth = [[0 for j in range(T+H+2)]for i in range(T+H+2)]
	hotels_visited = [False for i in range(H+1)]
	for h in range(1,H+1):
		neighbours[T+h] = []
	for t in range(1,T+1):
		hotels = [ int(i) for i in sys.stdin.readline().rstrip('\n').split() ]
		neighbours[t] = []
		for each_hotel in hotels[1:]:
			neighbours[t].append(T+each_hotel)
			neighbours[T+each_hotel].append(t)
			bandwidth[T+each_hotel][t] = 1
			bandwidth[t][T+each_hotel] = 1
	#sys.stdin = sys.__stdin__	
	#print(neighbours)
	
	#print(H)
	#print(bandwidth[4])
	#print(bandwidth)

	print(H - max_flow())
	#print(bandwidth)
