class Solution:
    # @param A : integer
    # @return a list of integers
    def flip(self, v):
    	return '0' if v == '1' else '1'
    def allComb(self,A):
    	if A == 1:
    		return ['0', '1']
    	#build on sub problem result
    	sub_result = self.allComb(A-1)
    	result = []
    	v = '0'
    	for i in sub_result:
    		result.append(v+i)
    		v = self.flip(v)
    		result.append(v+i)
    		#v = self.flip(v)
    	return result
    def grayCode(self, A):
    	result = self.allComb(A)
    	result = [int(i,2) for i in result]
    	return result

s = Solution()
A = 3
print(s.grayCode(A))