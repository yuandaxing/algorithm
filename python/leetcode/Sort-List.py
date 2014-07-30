class Solution:
    def MergeList1(self, left, right) :
        head = None
        tail = None
        while left or right :
            cur = None
            if left == None or (right and  left.val > right.val) :
                cur = right
                right = right.next
            else :
                cur = left
                left = left.next
            if head == None :
                head = cur
                tail = head
            else :
                tail.next = cur
                tail = tail.next
            cur.next = None
        return head
    def MergeList(self, left, right) :
        head = None
        tail = None
        if left == None or right == None :
            return left if left else right

        while left and right :
            cur = None
            if left.val > right.val :
                cur = right
                right = right.next
            else :
                cur = left
                left = left.next
            if head == None :
                head = cur
                tail = head
            else :
                tail.next = cur
                tail = tail.next
            cur.next = None

        tail.next = left if left else right
        return head

    # point to pointer maybe make it more concise to write
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        Nodes = [None for i in range(64)]
        while head :
            cur = head
            head = head.next
            cur.next = None
            for i in range(64) :
                if Nodes[i] :
                    cur = self.MergeList(cur, Nodes[i])
                    Nodes[i] = None
                else :
                    Nodes[i] = cur
                    break
        result = None
        for i in range(64) :
            result = self.MergeList(result, Nodes[i])
        return result

class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None

a = ListNode(1)
b = ListNode(3)
c = ListNode(2)
a.next = b
b.next = c

sol = Solution()
#myr = sol.MergeList(a, b)
#myr = sol.MergeList(myr, c)
myr = sol.sortList(a)
#myr = a
while myr :
    print myr.val
    myr = myr.next
string = 
