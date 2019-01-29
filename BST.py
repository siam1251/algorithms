#root has
class Node:
	"""docstring for ClassName"""
	def __init__(self,value=None,left=None, right=None,parent=None):
		self.left = left
		self.right = right
		self.value = value
		self.parent = parent
		self.dist = 0
		self.visited = False
		self.total_distance = None

def insert(current_root, node):
	if current_root.value == None:
		node.dist = 0
		current_root.value = node.value
		return

	value = current_root.value
	if node.value > value:
		if current_root.right == None:
			node.dist = current_root.dist + 1
			node.parent = current_root
			current_root.right =  node
			return
		else:
			insert(current_root.right,node)
	else: #current node is smaller or equal to root
		if current_root.left == None:
			node.dist = current_root.dist + 1
			node.parent = current_root
			current_root.left = node
			return
		else:
			insert(current_root.left,node)

def get_distance(current_dist,current_node):
	if current_node == None or current_node.visited == True:
		return 0
	elif current_node.total_distance != None:
		return current_node.total_distance + 1
	dist_left = 0
	dist_right = 0
	dist_parent = 0
	current_node.visited = True
	
	dist_left = get_distance(current_dist+1,current_node.left)
	dist_right = get_distance(current_dist+1,current_node.right)
	dist_parent = get_distance(current_dist+1,current_node.parent)
	
	total_dist = current_dist + dist_left + dist_right + dist_parent
	current_node.visited = False
	return total_dist

def get_dist(current_node, total_nodes):
	if current_node.parent == None:# root node
		current_node.total_distance = 0
		return 0
	else:
		current_node.total_distance = current_node.parent.total_distance + (total_nodes-1)
		return current_node.total_distance
	
def print_tree(root,str_):
	if root == None:
		return
	print(root.value,root.dist,end='')	
	if root.right != None:
		print('-------- ',end='')
		str_ +=' '*12
		print_tree(root.right,str_)
		str_ = str_[:-12]
	if root.left !=None:
		print()
		print(str_,end='')
		print('|')
		print(str_,end='')
		print('|')
		print(str_,end='')
		
		#print(root.left.value,root.left.dist)
		print_tree(root.left,str_)

root = Node()
a = [4]
s = 0
if __name__ == '__main__':
	#N = input()
	#a = [int(i) for i in input().split()]
	total_nodes = 0
	for i in a:
		total_nodes +=1
		node = Node(i)
		#print(node.value)
		insert(root,node)
		s +=get_dist(node,total_nodes)
		#node.total_distance = s
		print(s)
	print_tree(root,'')
