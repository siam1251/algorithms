class Solution:

    # @param A : list of integers
    # @param B : integer
    # @return a list of integers

    def dNums(self, A, B):
    	d = {}
    	u = []
    	A.append(-1)
    	for ind,i in enumerate(A):
    		
    		if sum(d.values()) < B:
    			if i in d.keys():
    				d[i] +=1
    			else:
    				d[i] = 1
    		else:#we have a window legth B
    			print(d)
    			r = filter(lambda x:x==1,d.values()) 
    			u.append(sum(r))
    			print(ind)
    			d[A[ind-B]] -=1
    			if d[A[ind-B]] == 0:
    				del d[A[ind-B]] 
    			if i in d.keys():
    				d[i] +=1
    			else:
    				d[i] = 1
    	return list(u)
s = Solution()
print(s.dNums([1, 2, 1, 3, 4, 3],3))



