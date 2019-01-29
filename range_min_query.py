def s_tree(n, l, r):
	if l == r:
		nodes[n] = numbers[l-1]
		return nodes[n]
	mid = (l+r)//2
	l_node = 2*n
	r_node = 2*n + 1
	left = s_tree(l_node,l,mid)
	right = s_tree(r_node, mid+1,r)
	nodes[n] = min(left,right)
	return nodes[n]

def query(n,l,r,start,end):
	if start > r or end < l:
		return 0
	if l>=start and r <= end:
		return nodes[n]

	mid = (l+r)//2
	l_node = 2*n
	r_node = 2*n+1
	return min(query(l_node,l,mid,start,end),query(r_node,mid+1,r,start,end))
	

if __name__ =='__main__':
	f = open('i1.txt','r')
	f = f.read().splitlines()
	
	N,M =[ int(i) for i in f[0].split() ]
	nodes = [0 for i in range(N*3)]

	numbers = [ int(i) for i in f[1].split()]
	queries = []
	s_tree(1,1,N)
	#print(query(1,1,N,2,3))
	for k in range(M):
		queries.append([int(i) for i in f[2+k].split()])
		#print(queries)
		#print(queries[k][0],queries[k][1])
		print(query(1,1,N,queries[k][0]+1,queries[k][1]+1))
	
	#print(nodes)
	


