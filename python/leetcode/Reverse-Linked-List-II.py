
class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    # @ tail point to previous node, maybe head
    # @ for m to n insert the element to tail.
    # @ for m+1, insert at n
    def reverseBetween(self, head, m, n):
        Tpivot, newHead = ListNode(0), head
        tail, nNode, newHead, Tpivot.next = Tpivot, Tpivot, Tpivot, newHead
        for i in range(m) :
            tail, nNode = nNode, nNode.next
        nextHead,tail.next = nNode, None
        for i in range(m, n+1) :
            cur, nextHead = nextHead, nextHead.next
            tail.next, cur.next = cur, tail.next
        nNode.next = nextHead
        return newHead.next

    def printList(self, head) :
        while head :
            print head.val
            head = head.next


            
        
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

t1, t2, t3, t4, t5 = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
t1.next = t2; t2.next = t3; t3.next = t4; t4.next = t5

sol = Solution()
sol.printList(sol.reverseBetween(t1, 2,4))
