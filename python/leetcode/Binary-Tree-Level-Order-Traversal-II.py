
class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    # @
    def levelOrderBottom(self, root):
        queue, res = [], []
        if not root : return res
        queue.append((root, 0))
        while len(queue) :
            cur = queue.pop(0) 
            if len(res) < cur[1]+1 : res.append([])
            res[cur[1]].append(cur[0].val)
            if cur[0].left : queue.append((cur[0].left, cur[1]+1))
            if cur[0].right : queue.append((cur[0].right, cur[1]+1))
        res.reverse()
        return res


#Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

t1, t2, t3, t4, t5 = TreeNode(3), TreeNode(9), TreeNode(20), TreeNode(15), TreeNode(7)
t1.left = t2; t1.right = t3; t3.left = t4; t3.right = t5;

sol = Solution()
print sol.levelOrderBottom(t1)
