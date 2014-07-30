# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    # @curQueue, nextQueue = [][]
    # @ curQueue.append(root)
    #  while len(curQueue) or len(nextQueue) 
    #     level = 0, res.append([])
    #     while curQueue :
    #         first = curQueue.pop(0)
    #         res[level].append(first)
    #         if first.left
    #            nextQueue.append(first.left)
    #         if first.right
    #            nextQueue.append(first.right)
    #     if level % 2 == 1
    #     res[level].reverse()
    #     level, curQueue, nextQueue = level+1, nextQueue, curQueue
    #
    def zigzagLevelOrder(self, root):
        level, curQueue, nextQueue = 0, [], []
        res = []
        if not root: return res
        curQueue.append(root)
        while len(curQueue) :
            res.append([])
            while len(curQueue) :
                first = curQueue.pop(0)
                res[level].append(first.val)
                if first.left : nextQueue.append(first.left)
                if first.right : nextQueue.append(first.right)
            if level%2 == 1: res[level].reverse()
            level, curQueue, nextQueue = level+1, nextQueue, curQueue
        return res
                
