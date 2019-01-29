class Solution:
	# @param A : tuple of integers
	# @return an integer
	def maxProduct(self, A):
		max_product = 1
		min_product = 1
		max_so_far = 1
		for i in A:
			#positive
			if i > 0:
				max_product = max_product*i,1
				min_product = min(min_product*i,1)
			#zero
			if i == 0:
				max_product = 1
				min_product = 1
			#negative
			else:
				
				tmp = max_product
				max_product = max(1,min_product*i)
				min_product = tmp*i

			if max_so_far < max_product:
				max_so_far = max_product








s = Solution()
print(s.maxProduct([  0,  0 ]))
