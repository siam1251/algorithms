
import sys
import copy
def get_index(seq_len, element):
	start = 0
	end = seq_len-1
	while ((end - start) > 0):
		mid = (end  +start)//2
		print(mid,start,end)
		if table[mid] > element:
			end = mid
		else:
			start = mid+1
	return start



def dp():
	table[0] = in_str[0]
	seq_len = 1
	for i in range(1,N):
		#print(seq_len)
		if table[0] > in_str[i]:
			table[0] = in_str[i]
		elif in_str[i] > table[seq_len-1]:
			table[seq_len] = in_str[i]
			seq_len += 1
		else:
			ind = get_index(seq_len, in_str[i])
			table[ind] = in_str[i]
	return seq_len


if __name__ == '__main__':
	f = open('input.txt', 'r+')                             
	sys.stdin = f  
	
	N = int(input())
	in_str = []
	try:
		while True:
			in_str.append(int(input()))
	except:
		pass
	#print(in_str)
	#print(sorted_str)
	N = len(in_str)
	print(N)
	table = [0 for i in range(N+1)]
	l = dp()
	print(l)
	# a = [1,2,3,4,5,6]
	# table = a
	# print(get_index(6,2))
