
import sys
max_dis = 9999

def get_min_distance():
	actual_dist = max_dis
	for l in roads.values():
		first_smallest = max_dis
		second_smallest = max_dis
		for d in l:
			if d < first_smallest:
				second_smallest = first_smallest
				first_smallest = d
			elif d < second_smallest:
				second_smallest = d
		current_dist = first_smallest+second_smallest
		if current_dist< actual_dist:
			actual_dist = current_dist
	return actual_dist

if __name__ == '__main__':
	f = open('i2.txt','r')
	sys.stdin = f  
	#f = f.read().splitlines()
	T = int(input())
	for t in range(T):
		[locations, r] = [ int(i) for i in input().split() ]
		#print(table)
		roads = {}
		for e in range(r):
			values =[ int(i) for i in input().split() ]
			#print(values)
			if values[0] not in roads:
				roads[values[0]] = []
			roads[values[0]].append(values[2])
			if values[1] not in roads:
				roads[values[1]] = []
			roads[values[1]].append(values[2])
		print(get_min_distance())
		#print('-------------------------------------')
		