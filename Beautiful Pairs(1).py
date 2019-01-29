def get_pairs():
	cnt = 0
	matched = [False for i in range(N)]
	
	
	for i in range(N):
		for j in range(N):
			if A[i] == B[j] and matched[j] == False:
				cnt+=1
				matched[j] = True
				break
	# prev = A[0]

	# sameA = True
	# for i in range(1,N):
	# 	if prev != A[i]:
	# 		sameA = False
	# 		break
	# prev = B[0]
	# sameB = True
	# for i in range(1,N):
	# 	if prev != B[i]:
	# 		sameB = False
	# 		break
	# if sameA == True or sameB == True:
	# 	return cnt-1
	if cnt == N:
		cnt -= 1
	elif cnt < N:
		cnt += 1
	return cnt

import sys
if __name__ == '__main__':
	f = open('i3.txt','r')
	sys.stdin = f  
	#f = f.read().splitlines()
	#print(f)
	N = int(input())
	A = [int(i) for i in input().split()]
	B = [int(i) for i in input().split()]
	pairs = get_pairs()
	

	print(pairs)
