class Solution:
    # @param A : list of integers
    # @return an integer
    def canJump(self, A):
    	i = len(A)-2
    	possible = [False for i in range(len(A))]
    	possible[len(A)-1] = True
    	while i >= 0:
    		for j in range(1,min(len(A)-A[i],A[i]+1)):
    			if possible[i+j] == True:
    				possible[i] = True
    				break
    		i-=1
    	#print(possible)
    	if possible[0] == True:
    		return 1
    	else:
    		return 0

s = Solution()
A = [ 25, 0, 27, 10, 0, 0, 29, 0, 0, 0, 17, 0, 6, 0, 0, 0, 0, 0, 0, 0, 15, 0, 20, 3, 0, 15, 22, 0, 0, 0, 23, 0, 0, 0, 0, 0, 0, 0, 0, 25, 0, 0, 8, 0, 0, 0, 13, 0, 10, 0, 0, 6, 0, 0, 18, 0, 25, 0, 0, 0, 28, 27, 0, 3, 2, 25, 0, 0, 20, 0, 16, 0, 0, 30, 0, 23, 20, 0, 0, 0, 12, 28, 15, 4, 0, 0, 17, 0, 0, 0, 21, 0, 0, 0, 0, 30 ]
print(s.canJump(A))
