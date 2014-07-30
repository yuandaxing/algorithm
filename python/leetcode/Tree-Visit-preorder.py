class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        if root :
            result = [root.val]
            result.extend(self.preorderTraversal(root.left))
            result.extend(self.preorderTraversal(root.right))
            return result
        else :
            return []
        
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

x = TreeNode(1)
y = TreeNode(2)
z = TreeNode(3)
x.right = y
y.left = z

sol = Solution()
print sol.preorderTraversal(x)
