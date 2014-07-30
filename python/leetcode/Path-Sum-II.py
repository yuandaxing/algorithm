
class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def __init__(self) :
        self.res = []
    def pathSumAux(self, root, sum, cur):
        if not root :
            return 
        sum -= root.val
        cur.append(root.val)
        if not root.left and not root.right :
            if not sum :
                self.res.append(list(cur)) 
        else :
            self.pathSumAux(root.left, sum, cur)
            self.pathSumAux(root.right, sum, cur)
        cur.pop()
                
    def pathSum(self, root, sum):
        self.pathSumAux(root, sum, [])
        return self.res


#Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

t1,t2,t3,t4,t5,t6,t7,t8,t9,t10 = TreeNode(5),TreeNode(4),TreeNode(8),TreeNode(11),TreeNode(13),TreeNode(4),TreeNode(7),TreeNode(2),TreeNode(5),TreeNode(1)
t1.left=t2; t1.right=t3; t2.left=t4; t3.left=t5; t3.right=t6
t4.left=t7; t4.right=t8; t6.left=t9; t6.right=t10;

sol = Solution()
print sol.pathSum(t1, 22)
