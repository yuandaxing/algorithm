# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    # @ cur = next, while next.val = cur.val, next = next.next
    # @ if cur.next == next : append one element
    # @ cur = next
    def deleteDuplicates(self, head):
        cur, next = head, head
        newHead, newTail = None, None
        while cur :
            while next and next.val == cur.val :
                next = next.next
            if cur.next == next :
                if not newTail :
                    newHead, newTail = cur, cur 
                else :
                    newTail.next = cur
                    newTail = cur
            cur = next
        if newTail :
            newTail.next = None 
        return newHead
