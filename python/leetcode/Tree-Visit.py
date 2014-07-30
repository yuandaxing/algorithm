class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        if root :
            left = self.postorderTraversal(root.left)
            right = self.postorderTraversal(root.right)
            left.extend(right)
            left.append(root.val)
            return left
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
print sol.postorderTraversal(x)
