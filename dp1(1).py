class Solution:

	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def coinchange2(self, A, B):
		
		tb = [ 0 for i in range(B+1)]
		tb[0] = 1
		for coin in A:
			for value in range(coin,B+1):
				tb[value] += tb[value-coin]
		print(tb)
		return tb[B]
	

s = Solution()
print(s.coinchange2([ 2, 5, 3, 6,7 ],10))

