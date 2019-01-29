class Solution:
	# @param A : integer
	# @return an integer
	def colorful(self, A):
		B = []
		while A != 0:
			B.append(A%10)
			A = A//10
		A = []
		while len(B) > 0:
			A.append(B.pop())

		i = 1
		#print(A)
		products = []
		while i <= len(A):
			start = 0
			while start < len(A):
				if start+i-1 >= len(A):
					break
				mul = 1
				for m in range(start,start+i):
					mul*=A[m]
				if mul in products:
					return 0
				else:
					products.append(mul)
				start+=1
			i+=1
		return 1
s = Solution()
print(s.colorful(3245))
