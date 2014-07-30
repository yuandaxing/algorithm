# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def symmetricHelper(self, left, right) :
        if left and right :
            return left.val == right.val and \
                self.symmetricHelper(left.left, right.right) \
                and self.symmetricHelper(left.right, right.left) 
        elif not left and not right :
            return True
        else :
            return False
    def isSymmetric(self, root):
        if root :
            return self.symmetricHelper(root.left, root.right) 
        else :
            return True
        
