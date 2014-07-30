
class Solution:
	# @return a ListNode
	def addTwoNumbers(self, l1, l2):
		c = 0
		head, tail = None, None
		while l1 or l2 or c:
			left, right = 0, 0
			if l1 :
				left = l1.val
				l1 = l1.next
			if l2 :
				right = l2.val
				l2 = l2.next
			v = (left + right + c) % 10
			c = (left + right + c) / 10
			n = ListNode(v)
			if head :
				tail.next = n
				tail = n;
			else :
				head, tail = n, n
		return head
	def printList( self, L ) :
	        while L :
		        print L.val
		        L = L.next

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

n1 = ListNode(2)
n2 = ListNode(4)
n3 = ListNode(3)
n1.next = n2; n2.next = n3
n4 = ListNode(5)
n5 = ListNode(6)
n6 = ListNode(4)
n4.next = n5; n5.next = n6

sol = Solution()
sol.printList( sol.addTwoNumbers(n1, n4))
