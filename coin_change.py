
import sys
def dp():
	
	for i in range(1,N+1):
		for j in range(1,M+1):
			new_coin = C[j-1]
			if i-new_coin >= 0:
				if i - new_coin == 0:
					table[i][j] = table[i][j-1]+table[i-new_coin][j]+1
				else:
					table[i][j] = table[i][j-1]+table[i-new_coin][j]

			else:
				table[i][j] = table[i][j-1]

if __name__ == '__main__':
	f = open('input.txt', 'r+')                             
	sys.stdin = f  
	line = input().split()
	N = int(line[0])
	M = int(line[1])

	C = input().split()
	C = [ int(i) for i in C]
	#print(C)
	table = [ [0 for i in range(M+1)] for j in range(N+1)]
	dp()
	print(table[N][M])
	

