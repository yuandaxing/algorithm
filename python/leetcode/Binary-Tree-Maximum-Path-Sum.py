
class Solution:
    # @param root, a tree node
    # @return an integer

    #floyd algorithm O(N^3) algorithm
    # 
    # design function, return 
    def maxPathSumAux(self, root):
        if root :
            right, left =(0, -10000), (0, -10000)
            if root.left :
                left = self.maxPathSumAux(root.left) 
            if root.right :
                right = self.maxPathSumAux(root.right) 
            curV = root.val
            #print left, right
            rootDepth = max(curV, curV+left[0], curV+right[0])
            rootPath = max(left[1], right[1], curV+left[0]+right[0],
                           rootDepth)
            return rootDepth, rootPath
        return 0, 0
    def maxPathSum(self, root) :
        return self.maxPathSumAux(root)[1]

#Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

T1 = TreeNode(-3)
sol = Solution()
print sol.maxPathSum(T1)
