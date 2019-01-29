class Solution:
    # @param A : string
    # @return an integer
    def minCut(self, A):
        L = len(A)
        tb = [[0 for i in range(L) ] for j in range(L)]
        d = [999 for i in range(L)]
        for i in range(L):
            tb[i][i] = 1
        d[0] = 0
        for i in range(L):# add a input gradually
            for j in range(0,i):#
                #we can extend
                if A[j] == A[i] :
                    if tb[j+1][i-1] == 1 or i-j == 1:
                        tb[j][i] = 1
                        if j-1>=0:
                            #another palindrome from j to i
                            d[i] = min(d[i],d[j-1]+1)
                        else:#j==0
                            d[i] = 0
                #didn't match
                else:
                    
                    #another partition
                    d[i] = min(d[i],d[i-1]+1)
                    
        # print(tb)    
        # print(d)    
        return d[L-1]
                    
                        
                    
                    
s = Solution()
print(s.minCut("AAAATTTAAAAA"))