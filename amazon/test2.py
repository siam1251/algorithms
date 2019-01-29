import sys
if __name__=='__main__':
    
    f = open('input.txt','r')
    sys.stdin = f
    if __name__ == '__main__':
        N = int(input())
        lst = []
        for i in range(N):
            t,d = [int(i) for i in (input().split())]
            lst.append(t+d)
        new_list = sorted(enumerate(lst),key = lambda x: x[1])
        
        n_lst = [1+i[0] for i in new_list]
        print(n_lst)
        