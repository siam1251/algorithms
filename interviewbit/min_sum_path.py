class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minimumTotal(self, A):
    	l = len(A)
    	if l < 2:
    		return A[0][0]
    	inf_v = 999999
    	# current_row = [[i, A[l-1][i]] for i in range(l)]
    	# next_row = [[l-2, inf_v] for i in range(l)]
    	values = [[inf_v for j in range(len(A[i]))] for i in range(len(A))]
    	values[l-1] = A[l-1]
    	#tb.sort(key = lambda x:x[1],reverse = True)
    	label = l-1
    	while label > 0:
    		for i in range(label+1):
    			#left most
    			if i < label:
	    			if values[label][i]+A[label-1][i] < values[label-1][i]:
	    					values[label-1][i] = values[label][i]+A[label-1][i]
    			if i > 0:
    				if values[label][i]+A[label-1][i-1] < values[label-1][i-1]:
    					values[label-1][i-1] = values[label][i]+A[label-1][i-1]
    		label-=1
    	
    	#print(values)
    	return values[0][0]

s = Solution()
A = [
     [2],
    [6,6],
   [7,8,4]
]
print(s.minimumTotal(A))
