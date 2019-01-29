# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def sum_path(self,A,s_total,B):
		if A.left == None and A.right == None:
			if s_total+A.val== B:
				return 1
			else:
				return 0
		
		if A.left != None:
			if self.sum_path(A.left,s_total+A.val,B) == 1:
				return 1
		if A.right != None:
			if self.sum_path(A.right,s_total+A.val,B) == 1:
				return 1
			else:
				return 0




	# @param A : root node of tree
	# @param B : integer
	# @return an integer
	def hasPathSum(self, A, B):
		s_total = 0
		return self.sum_path(A,s_total,B)
		
