import math
class Solution:
	# @param A : string
	# @return an intege

	def numDecodings(self, A):
		N = [0 for i in range(len(A))]
		N[0] = 1
		if A[0] == '0':return 0
		for i in range(1,len(A)):
			if A[i] != '0':#as a single char decode
				N[i] += N[i-1]
			elif int(A[i-1]+A[i]) > 26:
				return 0
			if int(A[i-1]+A[i]) <= 26 and  int(A[i-1]+A[i]) >= 10:
				if i > 1:
					N[i] += N[i-2]
				else:
					N[i] += 1


		return N[len(A)-1]

		




s = Solution()
print(s.numDecodings('875361268549483279131'))