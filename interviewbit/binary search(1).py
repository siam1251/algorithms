class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return a list of integers
	def search(self,A, B):
		start = 0
		end = len(A)-1
		while start <= end:
			#print(start,end)
			mid = (start+end)//2
			
			#print(A[i][j])
			if A[mid] == B:
				return [mid,mid]
			elif B < A[mid]: # in first halve
				end = mid -1
			else: # in the second halve
				start = mid+1
		return [end, -1]
	def search1(self,A, B):
		start = 0
		end = len(A)-1
		while start <= end:
			#print(start,end)
			mid = (start+end)//2
			
			#print(A[i][j])
			
			if B < A[mid]: # in first halve
				end = mid -1
			else: # in the second halve
				start = mid+1
		return [mid, -1]

	def search2(self,A, B):
		left = 0
		right = len(A) -1
		while left < right:
			mid = (left+right)//2
			if A[mid] > B:
				right = mid
				
			else:# mid is equal or greater
				left = mid +1

		return left
	def search3(self,A, B):
		left = 0
		right = len(A) -1
		while left <= right:
			mid = (left+right)//2
			if A[mid] < B:
				left = mid+1
			else:
				right = mid

		return left
	def search4(self,A,B):
		left = 0
		right = len(A)-1
		while left<=right:
			mid = (left+right)//2
			if A[mid] >= B:
				right = mid - 1
			else:# strictly B is greater than mid
				left = mid+1
			
		return right+1

	def searchRange(self, A, B):
		r = self.search(A,B)
		if r[1]!= -1:
			return [self.search(A,B-.4)[0]+1, self.search(A,B+.4)[0]]
		else:
			return [-1, -1]
s = Solution()
A = [1,2,2,3,3,4,4,4,4]
print(s.search1(A,4))
print(s.search4(A,4))
print(s.search4(A,1))