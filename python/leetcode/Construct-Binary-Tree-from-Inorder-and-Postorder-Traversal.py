# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        def buildTreeAux(left, right) :
            if left[0] >= left[1] :
                return None
            rightRoot = right[1]-1
            leftRoot = inorder.index(postorder[rightRoot])
            root = TreeNode(postorder[rightRoot])
            root.left = buildTreeAux([left[0], leftRoot],
                                     [right[0], right[0]+ \
                                           leftRoot-left[0]])
            root.right = buildTreeAux([leftRoot+1, left[1]],
                                      [right[0]+leftRoot-left[0],\
                                            right[1]-1])
            return root
        return buildTreeAux([0, len(inorder)], 
                            [0, len(postorder)])

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


sol = Solution()
sol.buildTree([1,2,3,4], [2,4,3,1])
