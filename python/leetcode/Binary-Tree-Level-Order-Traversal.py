# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        queue, res = [], []
        if not root : return res
        queue.append((root, 0))
        while len(queue) :
            cur = queue.pop(0) 
            if len(res) < cur[1]+1 : res.append([])
            res[cur[1]].append(cur[0].val)
            if cur[0].left : queue.append((cur[0].left, cur[1]+1))
            if cur[0].right : queue.append((cur[0].right, cur[1]+1))
        return res

