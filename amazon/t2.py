class Solution:
    def combinations(self,i,j):
        
            
        if i >= self.L:
           
            return 1
        if j >self.L:
            return 0            
        
        elif self.tb[i] != -1:
            return self.tb[i]
        if self.A[i:j] in self.B:
            print(i,j,'--')
            self.tb[j] = self.combinations(j,j+1) 
            if self.tb[j] == 1:
                return self.tb[j]
            self.tb[i] = self.combinations(i,j+1)
           
            return self.tb[i]
            
        else:
            self.tb[i] = self.combinations(i,j+1)
            return self.tb[i]
            
            
    # @param A : string
    # @param B : list of strings
    # @return an integer
    def wordBreak(self, A, B):
        
        self.A = A
        self.cnt = 0
        self.B = B
        self.L = len(A)
        self.tb = [-1 for i in range(self.L+1)]
        return self.combinations(0,1)



s = Solution()
A = "a"
B = [ "aaa" ]
print(s.wordBreak(A,B))