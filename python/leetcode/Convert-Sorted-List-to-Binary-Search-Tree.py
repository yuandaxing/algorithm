# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    # @ first get the length of the list N
    # @ mid = N / 2
    # @ left, right = N / 2, N - N / 2 - 1
    # @ creatBBST(head, N)
    # @    if N == 0 : return head, None
    #         head, left = creatBBST(head, N/2)
    #         cur = TreeNode(head.va)
    #         head, right = creatBBST(head.next, N - N/2-1)
    #         cur.left, cur.right = left, right
    #          return head, cur

    def creatBBST(self, head, N) :
        if N == 0 : return head, None
        head, left = self.creatBBST(head, N/2)
        cur = TreeNode(head.val)
        head, right = self.creatBBST(head.next, N-N/2-1)
        cur.left, cur.right = left, right
        return head, cur
    def sortedListToBST(self, head):
        count, cur = 0, head
        while cur :
            cur, count = cur.next, count+1
        return self.creatBBST(head, count)[1]
        
