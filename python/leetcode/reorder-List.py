class Solution:
	# @param head, a ListNode
	# @return nothing
	def lenList(self, head) :
		count = 0
		while head :
			count += 1
			head = head.next
		return count
	def reverse(self, head) :
		newHead = None
		while head :
			cur = head
			head = head.next
			cur.next = newHead
			newHead = cur
		return newHead
    def reorderList(self, head):
        if head == None or head.next == None :
            return head
        listLen = self.lenList(head)
        right = listLen / 2
        left = listLen - right
        count = 0
        leftList = head
        rightList = head
        while count < left-1 :
            count += 1
            rightList = rightList.next
        next = rightList.next
        rightList.next = None
        rightList = self.reverse(next)
        
        count = 0;
        while count < right :
            next = leftList.next
            nextr = rightList.next
            leftList.next = rightList
            rightList.next = next
            leftList = next
            rightList = nextr
            count += 1

        return head
#algorithm
# first split the list into two parts
# second reverse the other part
# splice the list
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

sol = Solution()
#myr = sol.MergeList(a, b)
#myr = sol.MergeList(myr, c)
myr = sol.reorderList(a)
while myr :
    print myr.val
    myr = myr.next
