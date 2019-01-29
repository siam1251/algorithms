class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):
    	stck = []
    	#A = A.replace('./','')
    	A = A.split('/')
    	#print(A)
    	for i in A:
    		if i == '.' or i == '':
    			continue
    		if i == '..':
    			if len(stck)>0:
    				stck.pop()
    		else:
    			stck.append('/'+i)
    	if len(stck) == 0:
    		stck.append('/')
    	return ''.join(stck)

s = Solution()
print(s.simplifyPath('/../'))



