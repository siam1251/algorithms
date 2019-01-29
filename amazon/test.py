
if __name__ == '__main__':
    T = int(input().strip())
    while T> 0:
        N = int(input().strip())
        grid = [[0 for i in range(N)] for j in range(N)]
        for i in range(N):
            tmp = input().strip().split()
            grid[i] = tmp.sort()
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
        