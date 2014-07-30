
class Solution:
    # @param root, a tree node
    # @return an integer
    def __init__(self) :
        self.sumLeaf = 0
    def auxSumNumbers(self, v, root) :
        if not root :
            return 
        v = v* 10 + root.val
        if (not root.left) and (not root.right) :
            self.sumLeaf += v
        self.auxSumNumbers(v, root.left)
        self.auxSumNumbers(v, root.right)
    def sumNumbers(self, root):
        self.auxSumNumbers(0, root)
        return self.sumLeaf
        
#Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t1.left = t2
t1.right = t3

sol = Solution()
print sol.sumNumbers(t1)
