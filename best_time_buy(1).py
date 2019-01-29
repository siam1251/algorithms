class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
    	if len(A) <= 1:
    		return 0
    	
    
    	min_index = 0
    	total_profit = 0

    	for index, i in enumerate(A):
    		#print(i,current_profit)
    		
    		if index > 0 and A[index]>A[index-1] :
    		    total_profit += A[index]-A[index-1]
    	
    	return total_profit

s = Solution()
print(s.maxProfit([1,2]))

 