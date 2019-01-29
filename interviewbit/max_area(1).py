class Solution:
	# @param A : list of list of integers
	# @return an integer
	def maximalRectangle(self, A):
		ret = -100
		count = [0 for i in range(len(A[0]))]
		count.append(-1)
		for i in range(len(A)):
			for j in range(len(A[0])):
				count[j] += 1
				if A[i][j] == 0:
					count[j] = 0
			#max area in a histogram
			stack = []
			stack.append([-1,-1])
			for index, value in enumerate(count):
				#current index is the right index which is smaller than the smallest index
				# in stack we have the smallest height 
				# we have to find the left and right index
				while stack[-1][1] > value:
					ind, val = stack.pop()
					
					ret = max(ret,val*(index-stack[-1][0]-1))
				stack.append([index,value])
		return ret

s = Solution()
A = [ [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  	  [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
  	  [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
  	  [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
]
print(s.maximalRectangle(A))





