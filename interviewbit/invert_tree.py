# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	
    # @param root : root node of tree
    # @return the root node in the tree
    def invertTree(self, root):
    	if root == None:
    		return
    	elif root.left != None or root.right !=None:
    		tmp = root.left
    		root.left = root.right
    		root.right = tmp
    	root.left = self.invertTree(root.left)
    	root.right = self.invertTree(root.right)
    	return root
