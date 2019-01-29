class Solution:
	def flip(self,A,index):
		for i in range(index+1, len(A)):

			if A[i] == 0:
				A[i] = 1
			else:
				A[i] = 0
				break
		#print(A)

	# @param A : list of integers
	# @return an integer
	def bulbs(self, A):
		cnt = 0
		index = 0
		for i in A:
			if i == 0:
				cnt+=1
				if cnt%2 != 0:
					self.flip(A,index)
			index += 1
		return cnt

s = Solution()
A = [0,1,0,1]
print(s.bulbs(A))
