

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        tail = head
        while n :
            tail, n = tail.next, n-1
        prev, cur = head, head
        while tail :
            tail, cur, prev = tail.next, cur.next, cur
        if prev == cur :
            return prev.next
        else :
            prev.next = cur.next
            return head
    def printList(self, head) :
        while head :
            print head.val
            head = head.next


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

L1 = ListNode(1)
L2 = ListNode(2)
L3 = ListNode(3)
L4 = ListNode(4)
L5 = ListNode(5)
L1.next = L2
L2.next = L3
L3.next = L4
L4.next = L5

sol = Solution()
k = sol.removeNthFromEnd(L1, 2)
sol.printList(k)
