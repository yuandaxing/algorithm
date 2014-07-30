 class ListNode {
     int val;
     ListNode next;
     ListNode(int x) {
         val = x;
         next = null;
     }
 }
public class RemoveFromTheLastK {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        // Start typing your Java solution below
        // DO NOT write main() function
    	ListNode cur = head;
    	for(int i = 1; i < n; i++){
    		cur = cur.next;
    	}
    	ListNode pre = null;
    	ListNode f = head;
    	while(cur.next != null){
    		pre = f;
    		f = f.next; 
    		cur = cur.next;
    	}
    	
    	if(pre == null){
    		ListNode second = f.next;
    		f.next = null;
    		return second;
    	}
    	pre.next = f.next;
    	return head;
        
    }
}
