package org.java.cgcl;


public class ReverseGroup {
    public ListNode reverseKGroup(ListNode head, int k) {
        // Start typing your Java solution below
        // DO NOT write main() function
    	if(k == 1)
    		return head;
    	
    	ListNode h = null;
    	ListNode cur = head;
    	ListNode prefirst = null;
    	while(cur != null){
    		int pos = 1;
    		ListNode first = cur;
    		for(; pos < k && cur != null; pos++){
    			cur = cur.next;
    		}
    		if(pos != k || cur == null)
    			break;
    		
    		while(first != cur){
    			ListNode pre = first;
				first = first.next;
    			if(prefirst != null){
    				prefirst.next = pre.next; //remove from the list
    			}
    			pre.next = cur.next;
				cur.next = pre;
    		}
    		
    		if(h == null)
    			h = cur;
    		
    		pos = 1;
    		for(; pos < k && cur != null; pos++){
    			cur = cur.next;
    		}
    		
    		prefirst = cur;
    		if(cur.next == null)
    			break;
    		cur = cur.next;
    	}
    	
    	if(h == null)
    		return head;
    	return h;
        
    }
    
    public ListNode swapPairs(ListNode head) {
        // Start typing your Java solution below
        // DO NOT write main() function
    	return reverseKGroup(head, 2);
    }
    
    public static void main(String[]args){
    	int[] A = {1,2,3,4,5,6};
    	ReverseGroup rg = new ReverseGroup();
    	AddTwoNumbers atn = new AddTwoNumbers();
    	ListNode arr = atn.getFromArray(A, 0);
    	atn.travel(rg.reverseKGroup(arr, 2));
    }
}
