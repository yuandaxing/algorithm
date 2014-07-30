# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head == None :
            return False
        cur = head
        cur2 = cur.next
        while cur and cur2 and cur2.next and cur != cur2 :
#            print cur.val, cur2.val
            cur = cur.next
            cur2 = cur2.next.next

        return cur != None and cur2 != None and \
                      cur2.next != None and cur == cur2


class ListNode :
    def __init__(self, x) :
        self.val = x
        self.next = None
x = ListNode(1)
y = ListNode(2)
z = ListNode(3)
x.next = y
y.next = z
#z.next = x
sol = Solution()
print sol.hasCycle(y)
