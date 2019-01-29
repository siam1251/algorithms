#import numpy as np
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, A):
        if len(A) == 1:
            return 1
        A = list(A)
        tb = [[0 for j in range(len(A)+1)]for i in range(len(A)+1)]
        
        
        
        A_sorted = [i for i in A]
        A_sorted.sort()
        
        #print(A_sorted)
        A_sorted.insert(0,0)
        A.insert(0,0)
        
        #print(np.shape(tb))
        for i in range(1,len(A)):
            for j in range(1,len(A)):
                if A[j]== A_sorted[i] and A_sorted[i] != A_sorted[i-1]:
                    tb[i][j] = max(tb[i-1][j-1]+1,tb[i-1][j],tb[i][j-1])
                else:
                    tb[i][j] = max(tb[i-1][j],tb[i][j-1])
        matched_list = []
        i = len(A)-1
        j = len(A)-1
        #print(tb)
        while i > 0 and j > 0:
            
            if tb[i][j] == tb[i-1][j]:
                i-=1
            elif tb[i][j] == tb[i][j-1]:
                j-=1
            elif tb[i][j] == tb[i-1][j-1]+1:
                matched_list.append(A_sorted[i])
                i-=1
                j-=1
        rt_lst = []
       
        for i in range(len(matched_list)-1,-1,-1):
            rt_lst.append(matched_list[i])
        #print(rt_lst)
        #print(tb)
        return len(rt_lst)
A =[ 14, 24, 18, 46, 55, 53, 82, 18, 101, 20, 78, 35, 68, 9, 16, 93, 101, 85, 81, 28, 78 ]

s = Solution()
print(s.lis(A))





