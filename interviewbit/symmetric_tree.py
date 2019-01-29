# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def checkSymmetric(self,left,right):
		if left == None and right == None:
			return 1
		elif left== None or right == None:
			return 0
		if left.val == right.val:
			if self.checkSymmetric(left.left,right.right) and self.checkSymmetric(left.right,right.left):
				return 1
			else:
				return 0
		else:
			return 0
	# @param A : root node of tree
	# @return an integer
	def isSymmetric(self, A):
		if A.left == None and A.right == None:
			return 1
		elif A.left== None or A.right == None:
			return 0
		return self.checkSymmetric(A.left,A.right)
