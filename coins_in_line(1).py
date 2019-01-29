class Solution:
	def get_maxcoin(self,i,j):
		if self.tb[i][j] != -1:
			return self.tb[i][j]
		if i >= len(self.A) or j >= len(self.A):
			return 0

		
		else:
			v1 = self.A[i] + (self.sumA[j]-self.sumA[i]- self.get_maxcoin(i+1,j)) #range i+1 to j discard i
			if i-1 >= 0:
				v2 = self.A[j] + (self.sumA[j-1]-self.sumA[i-1]- self.get_maxcoin(i,j-1))# range i to j-1 discard j
			else:
				v2 = self.A[j] + (self.sumA[j-1]- self.get_maxcoin(i,j-1))# range i to j-1 discard j
			if i==0 and j == 1:
				print(v1,v2)
			self.tb[i][j] = max(v1,v2)
			return self.tb[i][j]


	# @param A : list of integers
	# @return an integer
	def maxcoin(self, A):
		s = 0
		self.A = A
		self.sumA = []
		for i in A:
			s+=i
			self.sumA.append(s)

		self.tb = [[-1 for j in range(len(A))] for i in range(len(A))]
		# for i in range(len(A)):
		# 			self.tb[i][i] = A[i]
		# v = self.get_maxcoin(0,len(A)-1)
		# print(self.sumA)
		# import numpy as np
		# print(np.array(self.tb))
		# return v
		N = [0 for i in range(len(A))]
		N[0] = A[0]
		for i in range(1,len(A)):
			v1 = self.A[i] + (self.sumA[j]-self.sumA[i]- self.get_maxcoin(i+1,j)) #range i+1 to j discard i
			v2 = self.A[0] + (self.sumA[j-1]-self.sumA[i-1]- self.get_maxcoin(i,j-1))# range i to j-1 discard j
			N[i] = max(v1,v2)
		print(N)

		




A = [ 1, 100, 500, 10 ]
s = Solution()
print(s.maxcoin(A))