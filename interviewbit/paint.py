class Solution:
	# @param A : integer
	# @param B : integer
	# @param C : list of integers
	# @return an integer
	def isPossible(self,T,A,B,C):
		
		start = 0
		s = 0
		painter = B
		time_per_unit = C
		for i in A:
			if (s+i)*time_per_unit <= T:
				s = s+i
			else:
				s = i
				B -=1
				if B < 0 or s*time_per_unit > T:
					return False
		return True



	def paint(self, A, B, C):
		left = sum(A)*C/B
		right = sum(A)*C
		while left < right:
			mid = (left+right)//2
			if self.isPossible(mid,A,B,C):# it's possible but may not be best
			  right = mid
			else:
			  left = mid+1 # it won't stuck because left is increasing
		return right


s = Solution()
A = 3
B = 10
C = [ 640, 435, 647, 352, 8, 90, 960, 329, 859 ]
A = 2
B = 9
C = [1, 10]
print(s.isPossible(17220,C,A,B))
print(s.paint(C,A,B))