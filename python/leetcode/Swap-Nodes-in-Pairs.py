
class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        prev = ListNode(0)
        prev.next, head, cur = head, prev, head
        while cur :
            next = cur.next
            if next :
#                print cur.val, next.val
                prev.next, cur.next, next.next = next, next.next, cur
 #               print cur.val, next.val
            prev, cur = cur, cur.next
        return head.next
    def printList( self, L ) :
        while L :
            print L.val
            L = L.next

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


n1, n2 = ListNode(1), ListNode(2)
n1.next = n2
sol = Solution()
z = sol.swapPairs(n1)
sol.printList(z)
