# Definition for a  binary tree node

class Solution:
    # @param 
    # algorithm 2.
    # List1 = root
    # while List1 :
    #      while List1 and not List1.left and not List1.right :
    #         List1 = List1.next
    #      List2 = None if not List1 else (List1.left or List2.right)
    #      save = List1
    #      while List2 :
    #         while List1 and List1.right != List2 and :
    #         List1 = List1.next
    #
    #          
    #        
    def nextParentChild(self, root, cur) :
        while root and ((not root.left and not root.right) or \
                        (root.left == cur and not root.right) or \
                        (root.right == cur)) :
            root = root.next
        if not root :
            return None, None
        else :
            return root, root.left if root.left not in (None, cur) else root.right
    def connect(self, root):
        while root :
            parent, child = self.nextParentChild(root, None) 
            root, prev = child, child
            while parent :
                parent, child = self.nextParentChild(parent, child)
                prev.next, prev = child, child
                if parent and  parent.left == child and parent.right :
                    child, prev.next, prev = parent.right, parent.right, parent.right

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
                    
t1, t2, t3, t4, t5 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5)
t1.left = t2; t1.right = t3
t2.left = t4; t3.right = t5

sol = Solution()
print sol.connect(t1)
