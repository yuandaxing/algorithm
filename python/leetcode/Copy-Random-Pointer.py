## Definition for singly-linked list with a random pointer.
#
#class Solution:
#    # @param head, a RandomListNode
#    # @return a RandomListNode
#    def copyRandomList(self, head):
#        # add a new Node to the list
#        cur = head
#        while cur :
#            rln = RandomListNode()
#            rln.next = cur.next
#            cur.next = rln
#            cur = cur.next.next
#        # set the random pointer field
#        cur = head
#        while cur :
#            next = cur.next
#            next.random = cur.random.next
#            cur = next.next
#        # release the pointer field
#        newHead, newTail = None, None
#        cur = head
#        while cur :
#            next = cur.next
#            if not newTail :
#                newHead, newTail = next, next
#            else :
#                newTail.next = next
#                newTail = next
#            cur.next = next.next
#            cur = cur.next
#
#        return newHead

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

# Definition for singly-linked list with a random pointer.

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        # add a new Node to the list
        cur = head
        while cur :
            rln = RandomListNode(cur.label)
            rln.next = cur.next
            cur.next = rln
            cur = cur.next.next
        # set the random pointer field
        cur = head
        while cur :
            next = cur.next
            if cur.random :
                next.random = cur.random.next
            cur = next.next
        # release the pointer field
        newHead, newTail = None, None
        cur = head
        while cur :
            next = cur.next
            if not newTail :
                newHead, newTail = next, next
            else :
                newTail.next = next
                newTail = next
            cur.next = next.next
            cur = cur.next

        return newHead

        
