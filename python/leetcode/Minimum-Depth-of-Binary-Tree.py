# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if not root :
            return 0
        elif not root.left and not root.right :
            return 1
        elif root.left and root.right :
            return min(self.minDepth(root.left), 
                       self.minDepth(root.right))+1
        elif root.left :
            return self.minDepth(root.left) + 1
        else :
            return self.minDepth(root.right) + 1
                    
