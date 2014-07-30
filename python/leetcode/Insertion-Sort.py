class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertToSortList(self, head, node) :
        tail = head[1]
        prev = head[0]
        if tail and node.val > tail.val :
            tail.next = node
            node.next = None
            tail = node
            return (prev, tail)
        cur = prev
        while cur and cur.val < node.val :
            prev = cur
            cur = cur.next
        node.next = cur
        if cur == head[0] :
            return (node, tail if tail else node)
        else :
            prev.next = node
            return head
        
    def insertionSortList(self, head):
        result = (None, None)
        while head :
            cur = head
            head = head.next;
            cur.next = None
            result = self.insertToSortList(result, cur)
        return result[0]
            
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

x = ListNode(1)
y = ListNode(2)
z = ListNode(3)

x.next = z
z.next = y
sol = Solution()
r = sol.insertionSortList(x)
while r :
    print r.val
    r = r.next
