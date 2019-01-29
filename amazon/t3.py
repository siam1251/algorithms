class Solution:
    

    # @param A : list of list of chars
    # @return nothing
    def solveSudoku(self, A):
        AA = [list(i) for i in A]
        L = len(A)
        
        B = [ [A[i][j] for j in range(L)] for i in range(L)]
        

        
        values = [str(i) for i in range(1,10)]
        def rec(i,j):
           
            if j > L-1:
                i += 1
                j = 0
            if i > L-1:
                return True
           

            if AA[i][j] != '.':
                B[i][j] = AA[i][j]
                return rec(i,j+1)
            top_cells = [B[k][j] for k in range(L)]
            left_cells = [B[i][k] for k in range(L)]
            row_group = (i//3)*3 
            col_group = (j//3)*3 
            lst = []
            for ii in range(row_group,row_group+3):
                for jj in range(col_group,col_group+3):
                    if B[ii][jj] != '.':
                        lst.append(B[ii][jj])
            all_cells = top_cells+left_cells+lst

           
            possible_values = filter(lambda x: x not in all_cells, values)
            possible_values = list(possible_values)
            
            if len(possible_values) == 0:
                return False
            for v in possible_values:
                B[i][j] = v
                if rec(i,j+1) == True:
                        return True
                B[i][j] = ''
                
        rec(0,0)

        for i in range(L):
           A[i] = ''.join(B[i])
        return B
s = Solution()
A = [ "53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79" ]
s.solveSudoku(A)
print(A)