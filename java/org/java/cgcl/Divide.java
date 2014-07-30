package org.java.cgcl;

import java.util.Vector;

public class Divide {
	public static class Pair{
		int val;
		int k;
	}
    public int divide(int dividend, int divisor) {
        // Start typing your Java solution below
        // DO NOT write main() function
    	assert(divisor != 0);
    	boolean sig1 = true, sig2 = true;
    	if(dividend < 0){
    		dividend = 0 - dividend;
    		sig1 = false;
    	}
    	if(divisor < 0){
    		divisor = 0 - divisor;
    		sig2 = false;
    	}
    	boolean positive = (sig1 && sig2) || (!sig1 && !sig2) ;
    	int sum = 0;
    	int k = divisor;
    	int count = 1;
    	Vector<Pair> vp = new Vector<Pair>();
    	while(k < dividend){
    		Pair p = new Pair();
    		
    		p.val = k;
    		p.k = count;
    		vp.add(p);
    		
    		k += k;
    		count += count;
    	}

    	for(int i = vp.size() - 1; i >= 0; i--){
    		Pair p = vp.get(i);
    		if(p.val <= dividend){
    			dividend -= p.val;
    			sum += p.k;
    		}
    	}
    	if(!positive)
    		sum = 0 - sum;
    	return sum;
    }
    
    public static void main(String[] args){
    	Divide div = new Divide();
    	System.out.print(div.divide(100000000, 1));
    }

}
