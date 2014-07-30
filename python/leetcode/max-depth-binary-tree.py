###### Definition for a  binary tree node
###### class TreeNode:
######     def __init__(self, x):
######         self.val = x
######         self.left = None
######         self.right = None
#####
class Solution:
	# @param root, a tree node
	# @return an integer
	def maxDepth(self, root):
		m = 0
		if root :
			l = self.maxDepth(root.left)
			r = self.maxDepth(root.right)
			m = max(l, r) + 1
			
		return m

import os
print os.listdir("c:/")
