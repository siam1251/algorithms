# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def isSameTree(self, A, B):
    	if A == None and B== None:
    		return True
    	elif A == None or B == None:
    		return False

    	if A.val == B.val: #current value same
    		if isSameTree(A.left,B.left) and isSameTree(A.right,B.right):
    			return True
    		else:
    			return False

