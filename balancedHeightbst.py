# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def getHeight(self,A,depth):
		if A == None:
			return depth-1
		leftH = self.getHeight(A.left,depth+1)
		if leftH == -1:
			return -1
		rightH = self.getHeight(A.right,depth+1)
		if abs(leftH - rightH)>1:
			return 0
		else:
			return max(leftH,rightH)

	# @param A : root node of tree
	# @return an integer
	def isBalanced(self, A):
		if self.getHeight(A,0) == -1:
			return 0
		else:
			return 1
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.right = TreeNode(3)
root.right.right = TreeNode(1)
s = Solution()
print(s.isBalanced(root))