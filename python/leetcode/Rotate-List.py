# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def listLen(self, head) :
        count = 0
        while head :
            head, count = head.next, count+1
        return count

    def rotateRight(self, head, k):
        L = self.listLen(head)
        k = k % (L if L else 1)
        if not k :
            return head
        count = 0
        cur = head
        while count < k :
            count, cur = count+1, cur.next
        prevv, prev= head, head
        while cur :
            prevv, prev, cur = prev, prev.next, cur.next
            
        print prevv.val, prev.val 
        prevv.next = None
        newHead = prev 
        while prev.next :
            prev = prev.next
        prev.next = head
        return newHead
        
    def printList(self, head) :
        while head :
            print head.val
            head = head.next 

t1 = ListNode(1)
t2 = ListNode(2)
t1.next = t2
sol = Solution()
#sol.printList( sol.rotateRight(t1, 1))
sol.rotateRight(t1, 1)
