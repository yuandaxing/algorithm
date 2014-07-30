
class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    
    # return the last visite node
    #  
    def flattenAux(self, previous, root) :
        if not root: return None
        left, right, last = root.left, root.right, root
        if left :
            last = self.flattenAux(last, left)
        if right :
            last = self.flattenAux(last, right) 
        root.left = None
        if previous :
            previous.right = root
        return last
    def flatten(self, root):
        self.flattenAux(None, root)

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

t1, t2, t3 = TreeNode(1), TreeNode(2), TreeNode(3)
t4, t5 = TreeNode(4), TreeNode(5)
t4.right = t5; t5.left = t1
t1.left = t2; t1.right = t3
sol = Solution()
print sol.flatten(t4)
prev = t4
while t4:
    print t4.val
    
    if t4.left :
        print 'error'
    prev, t4 = t4, t4.right

