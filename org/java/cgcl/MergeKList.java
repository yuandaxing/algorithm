package org.java.cgcl;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.TreeSet;

/*class ListNode {
     int val;
     ListNode next;
     ListNode(int x) {
         val = x;
         next = null;
     }
 }*/
public class MergeKList {

    public ListNode mergeKLists(ArrayList<ListNode> lists) {
        // Start typing your Java solution below
        // DO NOT write main() function
    	TreeSet<ListNode> ts = new TreeSet<ListNode>(new  Comparator<ListNode>(){

			@Override
			public int compare(ListNode arg0, ListNode arg1) {
				// TODO Auto-generated method stub
				return arg0.val - arg1.val;
			}
    		
    	});
    	ListNode pre = null, list = null;;
    	for(ListNode ln : lists){
    		if(ln != null){
    			ts.add(ln);
    		}
    	}
        
    	while(!ts.isEmpty()){
    		ListNode min = ts.first();
    		ts.remove(min);
    		if(pre != null){
    			pre.next = min;
    		}
    		pre = min;
    		if(min.next != null){
    			ts.add(min.next);
    		}
    		pre.next = null;
    		if(list == null)
    			list = pre;
    	}
    	
    	return list;
    }
    
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        // Start typing your Java solution below
        // DO NOT write main() function
      ListNode pre = null, list = null, cur = null;
      if(l1 == null) return l2;
      if(l2 == null) return l1;
      
      while(l1 != null && l2 != null){
    	  if(l1.val > l2.val){
    		  cur = l2;
    		  l2 = l2.next;
    	  }else{
    		  cur = l1;
    		  l1 = l1.next;
    	  }
    	  cur.next = null;
    	  
    	  if(pre != null){
    		  pre.next = cur;
    	  }
    	  pre = cur;
    	  if(list == null){
    		  list = pre;
    	  }
      }
      
      if(l1 != null)
    	  pre.next = l1;
      if(l2 != null)
    	  pre.next = l2;
      return list;
    }
    public static void main(String[] args){
    	MergeKList mkl = new MergeKList();
    	AddTwoNumbers atn = new AddTwoNumbers();
    	int[] num1 = {1,2,2};
		int[] num2 = {1,1,2};
		ListNode li1 = atn.getFromArray(num1, 0);
		ListNode li2 = atn.getFromArray(num2, 0);
		ArrayList<ListNode> lists = new ArrayList<ListNode>();
		lists.add(li1);	lists.add(li2);
		atn.travel(mkl.mergeTwoLists(li1, li2));
    }
}
