# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def __init__(self) :
        self.result = []
    def postorderTraversal(self, root):
        if root :
            self.postorderTraversal(root.left)
            self.postorderTraversal(root.right)
            self.result.append(root.val)
            return self.result
        else :
            return []
