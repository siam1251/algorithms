import numpy as np
if __name__ == '__main__':
    T = int(input().strip())
    grid= []
    while T> 0:
        N = int(input().strip())
        grid = [[0 for i in range(N)] for j in range(N)]
        print(np.shape(grid))
        for i in range(N):
            tmp = list(input())
           
            grid[i] = sorted(tmp)
        ##
        flag = 0
       
        for i in range(N):
            C = [ grid[j][i] for j in range(N)]
            isSorted = [False if(C[i+1] < C[i]) else True for i in range(N-1)]
            if False in isSorted:
                print('NO')
                flag = 1
                break;
        if flag == 0:
            print('YES')
        