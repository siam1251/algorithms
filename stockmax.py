
import sys
def fix(i):
	for i in range(i,1,-1):
		if performance[i-1]> performance[i]:
			if candies[i-1]> candies[i]:
				break
			else:#problem
				candies[i-1]+=1

def dp(prices):
	if len(prices) <= 1:
		return 0
	maxInd = prices.index(max(prices))
	# print(max(prices))
	# print(prices.index(max(prices)))
	#return
	s = sum(prices[:maxInd])
	cnt = maxInd
	if maxInd == 0:
		return dp(prices[1:])
	return cnt*prices[maxInd]-s + dp(prices[maxInd:])




if __name__ == '__main__':
	f = open('input.txt', 'r+')                             
	sys.stdin = f  
	
	T = int(input())
	while T > 0:
		T -= 1
		N = int(input())
		prices = input().split()
		prices = [int(i) for i in prices]
		v = dp(prices)
		print(v)
		
	


