class Solution:
    # @param A : list of list of integers
    # @return an integer
    def adjacent(self, A):
    	sum1 = 0
    	sum2 = 0
    	if len(A[0]) == 1:
    		return max(A[0][0],A[1][0])
    	s1 = 0
    	N = [0 for i in range(len(A[0]))]
    	E = [max(A[0][i],A[1][i]) for i in range(len(A[0]))]
    	N[0] = E[0]
    	N[1] = max(E[0],E[1])
    	i = 2
    	while i < len(A[0]):

    		N[i] = max([E[i]+N[i-2],N[i-1]])
    		
    		i+=1
    	#print(E)
    	return N[len(E)-1]
s = Solution()
A = [[1, 2, 3, 4],
	[2, 3, 4, 5]]
print(s.adjacent(A))
A = list(A)
