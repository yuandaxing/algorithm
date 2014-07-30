# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        def buildTreeAux(left, right) :
            if left[0] >= left[1] :
                return None
            leftRoot = left[0]
            rightRoot = inorder.index(preorder[leftRoot])
            root = TreeNode(preorder[leftRoot])
            root.left = buildTreeAux([left[0]+1, left[0]+1+rightRoot-right[0]],
                                     [right[0], rightRoot])
            root.right = buildTreeAux([left[1]-right[1]+rightRoot+1, left[1]],
                                      [rightRoot+1, right[1]])
            return root
        return buildTreeAux([0, len(preorder)], 
                            [0, len(inorder)])
