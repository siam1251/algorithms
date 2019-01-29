class Solution:
    def num_partition(self,j):
        if self.d[j] != 999:
            return self.d[j]
        for i in range(j):
            if self.A[i] == self.A[j]:
                if self.tb[i+1][j-1] or j-i == 1:
                    self.tb[i][j] = 1
                    if i-1>= 0:
                        self.d[j] = min(self.d[j],self.num_partition(i-1)+1)
                    else: #j== 0
                        self.d[j] = 0
            else:#didn't match
                self.d[j] = min(self.d[j],self.num_partition(j-1)+1)
        return self.d[j]



    # @param A : string
    # @return an integer
    def minCut(self, A):
        L = len(A)
        self.A = A
        self.d = [999 for i in range(L)]
        self.d[0] = 0
        self.tb = [[0 for i in range(L)]for j in range(L)]
        for i in range(L):
            self.tb[i][i] = 1
        self.num_partition(L-1)        
        print(self.tb)    
        print(self.d)    
        return self.d[L-1]
                    
                        
                    
                    
s = Solution()
print(s.minCut("AAAATTTAAAAA"))