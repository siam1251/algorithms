class Solution:
	# @param A : string
	# @return an integer
	def seats(self, A):
		left = 0
		right = 0
		cur_left = -1
		
		for i, v in enumerate(A+'.'):
			if v == '.' :
				if cur_left != -1 and (right-left) < i+1 -cur_left:
					right = i
					left = cur_left
				cur_left = -1
				
			if v == 'x' and cur_left == -1:
				cur_left = i
		print(left,right)
		left_xs = 0
		for i in range(0,left):
			if A[i] == 'x':
				left_xs+=1
		right_xs = 0
		for i in range(right,len(A)):
			if A[i] == 'x':
				right_xs+=1
		move = 0
		
		
		#perfect condition
		i = left-1
		replace_pos = left-1
		while i >= 0:
			if A[i] == 'x':
				move += replace_pos-i
				replace_pos-=1
			i-=1
		#replacing the righ_xs
		i = right
		replace_pos = right
		while i < len(A):
			if A[i] == 'x':
				move += i - replace_pos
				replace_pos+=1
			i+=1

		return move


s = Solution()
A = '.xxxxx'
print(s.seats(A))