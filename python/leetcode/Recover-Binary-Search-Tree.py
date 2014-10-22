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
# algorithm 2:
#     every node return the smallest, biggest, the most lower two node 
#     which have not binary search tree properties
    
class Solution:
    # @param root, a tree node
    # @return a tree node
    def findLowestNode(self, root) :
        results = [None, None]
        left, right = list(results), list(results)
        if not root :
            return results
        if root.left :
            left = self.findLowestNode(root.left)
        if root.right :
            right = self.findLowestNode(root.right)
        lowerest = 
        leftsmallest = left[1] if root.left else root.val
        rightmost = rightmost[0] if root.right else root.val 
            
    def recoverTree(self, root):
        results = [None, None, None, None]
        left, right = list(results), list(results)
        if not root :
            return results
        if root.left :
            left = 
            
