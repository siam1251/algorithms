class Solution:
    # @param A : string
    # @return a list of list of strings
    def partition(self, A):
    	result = []
    	cur = []
    	self.find_combinations(result,cur,A,0)
    	print(result)

    def find_combinations(self,result,cur,A,i):
    	if len(A) == i:
    		result.append(cur)
    		#print(cur)

    	
    	for j in range(i,len(A)):
    		if self.isPalindrome(A[i:j+1]):
    			cur.append(A[i:j+1])
    			self.find_combinations(result,cur,A,j+1)
    			cur.pop()
    	

    def isPalindrome(self,A):
    	return list(A) == list(reversed(A))




s = Solution()
s.partition('aab')
