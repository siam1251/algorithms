class Solution:
	# @param A : tuple of integers
	# @return an integer
	def maxProduct(self, A):
		if len(A) == 1:
			return A[0]
		product = []
		product.append(1)
		first_negative = 1
		last_negative = 1
		ind = 0;
		length = 0
		num_negative = 0
		for index, i in enumerate(A):
			
			#negative
			if i < 0:
				length+=1
				num_negative+=1
				#check first negative occurs
				if first_negative > 0:
					first_negative = product[ind]*i
				product[ind]*=i
				last_negative = i
			#positive
			elif i > 0:
				length+=1

				product[ind]*=i
				last_negative*=i

			if i == 0 or len(A)-1 == index:
				#find the maximum in this split
				#more than one negative
				#print(product[ind])
				if product[ind] < 0:
					if num_negative > 0:
						if first_negative == last_negative == product[ind]:
							pass
						elif product[ind]/first_negative > product[ind]/last_negative:
							product[ind] = product[ind]/first_negative
						else:
							product[ind] = product[ind]/last_negative
					
				
				if length == 0:
					product[ind] = 0
				else:
					product.append(0)
					ind += 1
				if len(A)-1 != index:
					product.append(1)
					ind += 1
				#print(num_negative)
				num_negative = 0
				first_negative = 1
				last_negative = 1
				length = 0
		#print(first_negative,last_negative)
		#print(product)
		print(product)
		return max(product)




s = Solution()
print(s.maxProduct([  0,  0 ]))
