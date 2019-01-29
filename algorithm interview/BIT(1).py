# 2016, Sayem Mohammad Siam
#http://www.geeksforgeeks.org/binary-indexed-tree-or-fenwick-tree-2/
#http://cs.stackexchange.com/questions/10538/bit-what-is-the-intuition-behind-a-binary-indexed-tree-and-how-was-it-thought-a
#Binary index tree
# A is the array of cumulative sum of the elements of another array
# 
#
maxVal = 1
def update(idx,update_value,A,n):
	while idx <= maxVal:
		idx += (idx & -idx)
		A[idx] += update_value

# n is the size of array
def query(idx,A):
	s = 0
	while idx > 0:
		s += A[idx]
		idx -= (idx & -idx)

# Constructs and returns a Binary Indexed Tree for given
# array of size n.
def construct(arr, n):
 
    # Create and initialize BITree[] as 0
    A = [0]*(n+1)
 
    # Store the actual values in BITree[] using update()
    for i in range(n):
        updatebit(idx,arr[i],A,n)
 
    # Uncomment below lines to see contents of BITree[]
    #for i in range(1,n+1):
    #      print BITTree[i],
    return BITTree