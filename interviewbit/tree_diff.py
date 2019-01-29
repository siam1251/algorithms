def tree_diff(tree):



n = int(input())
v = input().split()
v = [int(i) for i in v]
v.append(0)
nodes_parent = [0 for i in range(n+1)]
nodes_value = [0 for i in range(n+1)]

for i in range(n):


