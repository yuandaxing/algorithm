# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @return a list of tree node
    def generate_range(self, left, right) :
        if left >= right :
            return [None]
        result = []
        for i in range(left, right) :
            for t1 in self.generate_range(left, i) :
                for t2 in self.generate_range(i+1, right) :
                    t = TreeNode(i) 
                    t.left = t1
                    t.right = t2
                    result.append(t)
        return result 

    def generateTrees(self, n):
        return self.generate_range(1, n+1)
