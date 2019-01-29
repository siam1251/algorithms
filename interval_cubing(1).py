def build_tree(node, l, r):
	if l == r:
		tree[node] = values[l-1]
		return tree[node]
	mid = (l+r)//2
	node_left = 2*node
	node_right = 2*node + 1
	tree[node] = build_tree(node_left,l,mid) + build_tree(node_right,mid+1,r)
	return tree[node]
def update(node, l,r, range_l, range_r):
	if range_r < l or range_l > r:
		return tree[node]
	elif l == r:#leaf node
		tree[node] = tree[node]**3
		return tree[node]
	else: # in the range, so we will divide and update
		mid = (l+r)//2
		node_left = 2*node
		node_right = 2*node+1
		tree[node] = update(node_left,l,mid,range_l, range_r)+update(node_right,mid+1,r,range_l, range_r)
		return tree[node]

def query(node, l,r, range_l, range_r):
	if range_r < l or range_l > r:
		return 0
	elif l >= range_l and r <= range_r:# l---r this part is inside of the given range
		return tree[node]
	else:
		mid = (l+r)//2
		node_left = 2*node
		node_right = 2*node+1
		return query(node_left,l,mid,range_l, range_r)+query(node_right,mid+1,r,range_l, range_r)
import sys
if __name__ == '__main__':
	f = open('i1.txt','r')
	sys.stdin = f  
	#f = f.read().splitlines()
	N = int(input())
	values = input()
	values =[ int(i) for i in values.split() ]
	N = len(values)
	tree = [0 for i in range(N*3)]
	propagate = [False for i in range(N*3)]
	build_tree(1,1,N)
	# print(tree)
	# print(values)
	# print(query(1,1,N,2,3))
	T = int(input())
	for line in range(T):
		line = input()
		
		numbers =[ int(i) for i in line.split() ]
		#print(numbers)
		if numbers[0] == 1:
			print(query(1,1,N,numbers[1],numbers[2])%95542721)
		else:
			update(1,1,N,numbers[1],numbers[2])