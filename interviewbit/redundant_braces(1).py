class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
    	operators = ['+','*','-','/']
    	braces = ['(',')']
    	stck = []
    	stckOpening = []
    	stckClosing = []
    	for i in A:
    		if i in operators or i in braces:
    			if i == ')':
    				op_cnt = 0
    				if stck[-1] in operators:
    					stck.pop()
    					op_cnt+=1

    				if stck[-1] != '(' or op_cnt == 0:
    					return 1
    				else:
    					stck.pop()
    			else:
    				stck.append(i)

    	return 0
s = Solution()
print(s.braces('((a+b)+c)'))


