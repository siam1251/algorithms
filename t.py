if __name__ == '__main__':
    N,K = [int(i) for i in input().strip().split()]
    numbers = [int(i) for i in input().strip().split()]
    #sorted_numbers = sorted(enumerate(numbers),key=lambda x:x[1],reverse=True)
    sorted_numbers = list(enumerate(numbers))
    for j in range(1,K+1):
        for i in range(len(numbers)-1,j):
            if numbers[i]>numbers[i-1]:
                swap(sorted_numbers[i],sorted_numbers[i-1])
    for i in range(K):   
        index = sorted_numbers[i][0]
        tmp = numbers[index]
        numbers[index] = numbers[i]
        numbers[i] = tmp
    numbers = [str(i) for i in numbers]
    numbers = ' '.join(numbers)
    print(numbers)
        
        