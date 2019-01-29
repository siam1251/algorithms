import math
class Solution:
	# @param A : string
	# @return an integer
	
	def nCr(self,n,r):
	    f = math.factorial
	    return f(n) / f(r) / f(n-r)

	def numDecodings(self, A):
		total = 0
		#find continuous
		i = 1
		nn = 1
		while i < len(A):
			
			length = 0
			while int(A[i-1]+A[i]) <= 26:
				if A[i] == '0':
					length-=1
					break
				length += 1
				i+=1
			if length > 0:
				total+=1
				nn*=length

			if A[i] == '0' and int(A[i-1]+A[i]) > 26:
				return 0
			i+=1

		comb = 1
		#total = 2
		print(total)
		print(nn)
		
		if A[0] == '0':
			return 0
		for i in range(total):
			# up = 1
			# down = 1
			# for j in range(i):
			# 	up *= total
			# 	down*=(j+1)
			# 	#print('f')
			#print(up/down)
			comb += self.nCr(total,i)
		return comb




s = Solution()
print(s.numDecodings('875361268549483279131'))