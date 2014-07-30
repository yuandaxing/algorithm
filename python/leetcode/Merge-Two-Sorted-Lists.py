# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        newHead, newTail, cur = None, None, None
        while l1 or l2 :
            if not l1 :
                cur, l2 = l2, l2.next
            elif not l2 :
                cur, l1 = l1, l1.next
            elif l1.val > l2.val :
                cur, l2 = l2, l2.next
            else :
                cur, l1 = l1, l1.next
            
            if not newHead :
                newHead, newTail = cur, cur
            else :
                newTail.next, newTail = cur, cur
        
        if newTail :
            newTail.next = None
        return newHead
                
                
