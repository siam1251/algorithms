
import sys
def fix(i):
	for i in range(i,1,-1):
		if performance[i-1]> performance[i]:
			if candies[i-1]> candies[i]:
				break
			else:#problem
				candies[i-1]+=1

def dp():
	candies[0] = 1
	for i in range(1,N):
		if performance[i-1]> performance[i]:
			if candies[i-1]>1:
				candies[i] = 1
				continue
			else:# have to fix all the previoius items
				candies[i-1] += 1
				fix(i-1)
				candies[i] = 1
		elif performance[i] > performance[i-1]:
			candies[i] = candies[i-1] + 1
		else:
			candies[i] =  1



if __name__ == '__main__':
	f = open('input.txt', 'r+')                             
	sys.stdin = f  
	
	N = 11#int(input())
	performance = []
	for i in range(N):
		performance.append(int(input()))
	#print(C)
	candies = [0 for i in range(N)]
	#print(candies)
	print(performance)
	dp()
	print((candies))
	print(sum(candies))
	


