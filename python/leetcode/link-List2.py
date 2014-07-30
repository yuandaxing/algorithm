class Solution:    
    def CycleNode(self, head):
        if head == None :
            return None
        cur = head
        cur2 = cur.next
        while cur and cur2 and cur2.next and cur != cur2 :
#            print cur.val, cur2.val
            cur = cur.next
            cur2 = cur2.next.next

        if cur and cur2 and cur2.next and cur == cur2 :
            return cur
        else :
            return None

    def lenList(self, head) :
        count = 0
        while head :
            count += 1
            head = head.next
        return count
    def detectCycle(self, head):
        cycleNode = self.CycleNode(head)
        if cycleNode == None :
            return None
        nextC = cycleNode.next
        cycleNode.next = None
        len1 = self.lenList(head)
        len2 = self.lenList(nextC)
        first, second = head, nextC
        skip = abs(len1 - len2)
        if len1 < len2 :
            first, second = second, first
        while skip > 0 :
            first = first.next
            skip -= 1

        while first != second :
            first = first.next
            second = second.next

        cycleNode.next = nextC
        return first


class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None

a = ListNode(1)
b = ListNode(3)
c = ListNode(2)
d = ListNode(4)
a.next = b
b.next = c
c.next = d
d.next = None

sol = Solution()
#myr = sol.MergeList(a, b)
#myr = sol.MergeList(myr, c)
myr = sol.detectCycle(a)
print myr, sol.CycleNode(a)
            
