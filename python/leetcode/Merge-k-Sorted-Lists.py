class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        newHead, newTail, cur = None, None, None
        while l1 or l2 :
            if not l1 :
                cur, l2 = l2, l2.next
            elif not l2 :
                cur, l1 = l1, l1.next
            elif l1.val > l2.val :
                cur, l2 = l2, l2.next
            else :
                cur, l1 = l1, l1.next
            
            if not newHead :
                newHead, newTail = cur, cur
            else :
                newTail.next, newTail = cur, cur
        
        if newTail :
            newTail.next = None
        return newHead
    #  a list of ListNode
    # @return a ListNode
    def mergeKListsAux(self, lists, start, end) :
        if end - start <= 0:
            return None
        elif end - start == 1 :
            return lists[start]
        elif end - start == 2 :
            return self.mergeTwoLists(lists[start], lists[start+1])
        mid = (start + end) / 2
        return self.mergeTwoLists(self.mergeKListsAux(lists, start, mid),
                                  self.mergeKListsAux(lists, mid, end))
    def mergeKLists(self, lists):
        return self.mergeKListsAux(lists, 0, len(lists))
