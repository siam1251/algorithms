import numpy as np

c = int(raw_input())
for i in range(c):
	N,K = raw_input().split()
	N = int(N)
	K = int(K)
	values = raw_input().split()
	values = [ int(value) for value in values]
	#table = [[0]*(N+1)]*(K+1)
	#table = [a]*(K+1)
	#print table
	table =  [ [0 for i in range(N+1)] for i in range(K+1)]
	for i in range(1,K+1):
		for j in range(1,N+1):
			new_value = values[j-1]
			if new_value > i:
				table[i][j] = table[i][j-1]
			else:

				if i-new_value >= 0:
					op1 = table[i-new_value][j]+new_value
					table[i][j] = max(op1, table[i-1][j], table[i][j-1])
				else:
					table[i][j] = max(new_value,table[i-1][j], table[i][j-1])
				# dif1 = i - op1
				# op2 = table[i-1][j]
				# dif2 = i - op2
				# op3 = table[i][j-1]
				# dif3 = i - op3
				# if dif1 < dif2 and dif1 < dif3:
				# 	choose = op1
				# elif dif2 < dif3 and dif2 < dif3:
				# 	choose = op2
				# else:
				# 	choose = op3
				#table[i][j] = choose
	print int(table[i][j])
	print table[:,1]
	#print table
