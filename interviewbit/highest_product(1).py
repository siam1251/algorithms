class Solution:
    # @param A : list of integers
    # @return an integer
    def maxp3(self, A):
    	negatives = filter(lambda x: x < 0,A)
    	positives = filter(lambda x: x >= 0,A)
    	
    	negatives = sorted(negatives)
    	positives = sorted(positives,reverse=True)
    	if len(A) == 3:
    		return A[0]*A[1]*A[2]
    	
    	max_value =-999
    	if len(negatives) >=2:
    		if len(positives) >= 1:
    			max_value = negatives[0]*negatives[1]*positives[0]
    		elif len(negatives)>=3:
    			max_value = negatives[-1]*negatives[-2]*negatives[-3]
    	if len(positives)>=3:
    		if max_value < positives[0]*positives[1]*positives[2]:
    			max_value = positives[0]*positives[1]*positives[2]
    	return max_value


s = Solution()
A = [ 0, -1, 3, 100, 70, 50 ]
print(s.maxp3(A))