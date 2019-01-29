class Solution:
	# @param A : list of list of integers
	# @return an integer
	def uniquePathsWithObstacles(self, A):
		tb = [[0 for i in range(len(A[0]))] for j in range(len(A))]
		#print(tb[0][1])
		if A[0][0] != 1:
			tb[0][0] = 1
		for i in range(len(A)):
			for j in range(len(A[0])):
				if A[i][j] != 1:
					if i-1 >=0:
							tb[i][j] += tb[i-1][j]
					if j-1 >= 0:
						#print(i,j)
						tb[i][j] += tb[i][j-1]
		#print(tb)
		return tb[len(A)-1][len(A[0])-1]



A = [
  [1,0]
]
s = Solution()
print(s.uniquePathsWithObstacles(A))