# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def insertAtHead(self, n, head) :
        n.next = head
        return n
        
    def partition(self, head, x):
        less, more, cur = None, None, head
        while cur :
            next = cur.next 
            if cur.val < x :
                less = self.insertAtHead(cur, less)
            else:
                more = self.insertAtHead(cur, more)
            cur = next
        result = None
        while more :
            next = more.next
            result = self.insertAtHead(more, result)
            more = next                
        while less :
            next = less.next
            result = self.insertAtHead(less, result)
            less = next
        return result 





                
