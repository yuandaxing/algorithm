# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#algorithm 1:
    # first push all the element into a list by inorder
    # then sort the array
    # inorder visit the tree, then if the element is not equal to the 
     # array, change the values
# algorithm 2: could not work
#     every node return the smallest, biggest, the most lower two node 
#     which have not binary search tree properties
    
class Solution:
    # @param root, a tree node
    # @return a tree node
    def inorderVisit(self, root, contradict) :
        if not root :
            return contradict
        curcon = contradict
        curcon = self.inorderVisit(root.left, curcon)
        v1, v2 = curcon[0], curcon[1]
        if not v1 :
            curcon = [root, None]
        else:
            if root.val < v1.val :
                curcon = [v1, root]
            else :
                curcon = curcon if v2 else [root, None]
        return self.inorderVisit(root.right, curcon)
    def recoverTree(self, root):
        z = self.inorderVisit(root, [None, None])
        v1, v2 = z[0], z[1]
        v1.val, v2.val = v2.val, v1.val
        return root

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
t1, t2, t3 = TreeNode(1), TreeNode(2), TreeNode(3)
t1.left = t2
t2.left = t3
s = Solution()
s.recoverTree(t1)
