def find_triplets(A,i,still_need):

	cnt = 0
	ret_lst = []
	if i == 0:
		return []
	if still_need == 1:
		cnt = 0
		for j in range(0,i):
			if int(A[j]) < int(A[i]):
				cnt+=1
				ret_lst.append(A[j])
		return ret_lst
	cur = i-1
	while(cur >= 0 ):
		if int(A[i]) > int(A[cur]):#we are taking cur value in the triplet
			for lst in find_triplets(A,cur,still_need-1):
				ret_lst.append(lst+A[cur])
		cur-=1
	return ret_lst



if __name__ =='__main__':
	
	c = input()
	A = input().split()
	A.append(str(999999999999999))
	print(len(set(find_triplets(A,len(A)-1,3))))



