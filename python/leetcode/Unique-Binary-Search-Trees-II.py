# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @return a list of tree node
    def numFac(self, n):
        res = 1
        for i in range(1, n+1):
            res *= i
    def generateTrees(self, n):
        return self.numFac(2*n) / (self.numFac(n) * self.numFac(n) * (n+1))

