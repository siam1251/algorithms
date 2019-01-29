class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
    	N = 32
    	r = 0
    	for i in range(N):
    		b = (A>>i)&1
    		r = r|b<<(N-i-1)
    	return r


sol = Solution()
print(sol.reverse(15))