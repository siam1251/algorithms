class Solution:
	# @param ratings : list of integers
	# @return an integer
	def candy(self, ratings):
		ratings.insert(0,-9)
		A = [1 for i in range(len(ratings))]
		A[0] = 0
		i = 1
		for i in range(1,len(ratings)):
			if ratings[i] > ratings[i-1]:
				A[i] = A[i-1]+1
		for i in range(len(ratings)-2,0,-1):
			if ratings[i] > ratings[i+1]:
				A[i] = max(A[i+1]+1,A[i],1)
			
		
		return sum(A)

s = Solution()
print(s.candy([81,1,2,3,3,2,1,1,1,-1,-2,-2,-2]))

