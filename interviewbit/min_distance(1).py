import numpy as np
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def minDistance(self, A, B):
    	A = ' '+A
    	B = ' '+B
    	tb = [[0 for j in range(len(A))]for i in range(len(B))]
    	tb[0] = [i for i in range(len(A))]
    	for i in range(len(B)):
    		tb[i][0] = i
    	for i in range(1,len(B)):
    		for j in range(1,len(A)):
    			if A[j] == B[i]:
    				tb[i][j] = min(tb[i-1][j-1],tb[i-1][j]+1,tb[i][j-1]+1)
    			else:
    				tb[i][j] = min(tb[i-1][j]+1,tb[i][j-1]+1,tb[i-1][j-1]+1)
    	#print(tb)
    	#print(np.shape(tb))
    	return tb[len(B)-1][len(A)-1]

s = Solution()
A = "Anshuman"
B = "Antihuman"
s.minDistance(A,B)
