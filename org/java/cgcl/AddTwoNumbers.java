package org.java.cgcl;

import java.math.BigInteger;

class ListNode {
    int val;
     ListNode next;
     ListNode(int x) {
         val = x;
         next = null;
     }
 }
public class AddTwoNumbers {

	BigInteger getBigInteger(ListNode head){
		BigInteger factor = new BigInteger(1+"");
		BigInteger sum = new BigInteger(0+"");
		while(head != null){
			BigInteger inte = (new BigInteger(head.val+"")).multiply(factor);
			sum = sum.add(inte);
			factor = factor.multiply(new BigInteger(10+""));
			head = head.next;
		}
		//System.out.print(sum.intValue()+"\t");
		return sum;
	}
	
	//we need recursive to solve
	public ListNode getList(BigInteger bi){
		if(bi.equals(new BigInteger(0+"")))
			return null;
		BigInteger factor = new BigInteger(10+"");
		BigInteger[] dr = bi.divideAndRemainder(factor);
		ListNode  li = getList(dr[0]);
		ListNode cur = new ListNode(dr[1].intValue());
		cur.next = li;
		return cur;	
	} 
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        // Start typing your Java solution below
        // DO NOT write main() function
    	BigInteger a = getBigInteger(l1);
    	BigInteger b = getBigInteger(l2);
    	BigInteger sum = a.add(b);
    
    	ListNode spec = new ListNode(0);
    	spec.next = null;
    	ListNode li=  getList(sum);
    	return li == null ? spec : li;
    }
	/**
	 * @param args
	 */
    
    public void travel(ListNode li){
    	while(li != null){
    		System.out.print(li.val +"\t");
    		li = li.next;
    	}
    }
    public ListNode getFromArray(int[] num, int start){
    	if(num.length <= start)
    		return null;
    	ListNode li = new ListNode(num[start]);
    	li.next = getFromArray(num, start+1);
    	return li;
    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		AddTwoNumbers atn = new AddTwoNumbers();
		int[] num1 = {2 , 4 , 3};
		int[] num2 = {5,  6 ,  4};
		ListNode li1 = atn.getFromArray(num1, 0);
		ListNode li2 = atn.getFromArray(num2, 0);
		ListNode li3 =  atn.addTwoNumbers(li1, li2);
		atn.travel(li3);
		
	}

}
