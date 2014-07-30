# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    # @ if cur.val == tail.val then cur = cur.next
    # @ else insert at the tail, tail = tail.next
    # @
    def deleteDuplicates(self, head):
        tail, newHead = None
        while head :
            if not newHead :
                tail, newHead = head, head 
            elif tail.val != head.val :
                tail.next = head 
                tail = tail.next
            head = head.next
        if not tail :
            tail.next = None
        return newHead
                
