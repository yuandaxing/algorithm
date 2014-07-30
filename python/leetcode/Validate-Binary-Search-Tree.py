
class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBSTAux(self, root, minV, maxV) :
        if not root : 
            return True
#        print root.val, minV, maxV
        if (minV != None and root.val <= minV) or \
           (maxV != None and root.val >= maxV) :
            return False
        return self.isValidBSTAux(root.left, minV, root.val) and \
            self.isValidBSTAux(root.right, root.val, maxV)
    
    def isValidBST(self, root):
        return self.isValidBSTAux(root, None, None)

sol = Solution()
print sol.isValidBST(None)


#Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

t1, t2 = TreeNode(0), TreeNode(-1)
t1.right = t2
print sol.isValidBST(t1)
