package org.java.cgcl;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.BitSet;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;

public class ThreeSum {
	
static public class ValWrapper{
	ArrayList<Integer> ali = null;
	public ValWrapper(ArrayList<Integer> v){
		ali = v;
	}
	public boolean equals(Object o)   
    {   
        if (this == o)   
        {   
            return true;   
        }   
        ValWrapper vw = (ValWrapper) o;
        if(ali.get(0).equals(vw.ali.get(0)) && ali.get(1).equals(vw.ali.get(1)))
        	return true;
        return false;
}
	public int hashCode() {
			return ali.get(0).intValue() *41 + ali.get(1).intValue();
	}
}
	private HashSet<ValWrapper> lookTable = new HashSet<ValWrapper>();
	boolean contain(int[] num, int start, int s){
		if(start > num.length - 1)
			return false;
		int right = num.length - 1;
		while(right >= start){
			int mid  = (right + start) / 2;
			if(num[mid] == s)
				return true;
			else if(num[mid] > s)
				right = mid - 1;
			else
				start = mid + 1;
		}
		return false;
	}
	
    @SuppressWarnings("unchecked")
	public ArrayList<ArrayList<Integer>> threeSum(int[] num) {
        // Start typing your Java solution below
        // DO NOT write main() function
    	ArrayList<ArrayList<Integer>> aali = new ArrayList<ArrayList<Integer>>();
        if(num.length < 3)
        	return aali;
        Arrays.sort(num);
        
        
        for(int i = 0; i < num.length -2; i++){
        	for(int j = i+1; j < num.length - 1; j++){
        		int s = 0 - ( num[i] + num[j]);
        		if(s < num[j]) break;
        		if(contain(num, j+1, s)){
        			ArrayList<Integer> ali = new ArrayList<Integer>();
        			ali.add(new Integer(num[i]));
        			ali.add(new Integer(num[j]));
        			ali.add(new Integer(s));
        			aali.add(ali);
        			}
        	}
        }
        Comparator compare = new Comparator<ArrayList<Integer>>(){
			@Override
			public int compare(ArrayList<Integer> o1, ArrayList<Integer> o2) {
				// TODO Auto-generated method stu
					return o1.get(0).compareTo(o2.get(0)) != 0  ? o1.get(0).compareTo(o2.get(0)) 
							: o1.get(1).compareTo(o2.get(1));
			}
        };
        
        Collections.sort(aali, compare);
        ArrayList<ArrayList<Integer>> ret = new ArrayList<ArrayList<Integer>>();
        if(aali.size() < 1) 
        	return ret;
        
        ret.add(aali.get(0));
        ArrayList<Integer> pre = aali.get(0);
        for(int i = 1; i < aali.size(); i++){
        	if(compare.compare(aali.get(i), pre) != 0)
        		ret.add(aali.get(i));
        	pre = aali.get(i);
        }
        return ret;
    }
    
    public ArrayList<ArrayList<Integer>> threeSum2(int[] num) {
        // Start typing your Java solution below
        // DO NOT write main() function
    	ArrayList<ArrayList<Integer>> aali = new ArrayList<ArrayList<Integer>>();
        if(num.length < 3)
        	return aali;
        Arrays.sort(num);
        
        
        for(int i = 0; i < num.length -2; i++){
        	for(int j = i+1; j < num.length - 1; j++){
        		int s = 0 - ( num[i] + num[j]);
        		if(s < num[j]) break;
        		if(contain(num, j+1, s)){
        			ArrayList<Integer> ali = new ArrayList<Integer>();
        			ali.add(new Integer(num[i]));
        			ali.add(new Integer(num[j]));
        			ali.add(new Integer(s));
        			if(aali.size() == 0){
        				aali.add(ali);
        				lookTable.add(new ValWrapper(ali));
        			}else{
        				if(lookTable.contains(new ValWrapper(ali)))
        					continue;
        				lookTable.add(new ValWrapper(ali));
        				aali.add(ali);
        			}
        			
        		}
        	}
        }
        return aali;
    }
	/**
	 * @param args
	 */
    
    public void printf(ArrayList<ArrayList<Integer>> aali){
    	for(ArrayList<Integer> ali : aali){
    		for(Integer inte : ali){
    			System.out.print(inte + "\t");
    		}
    		System.out.println();
    	}
    }
    
	public static void main(String[] args) {
		// TODO Auto-generated method stub
	int [] num = {3,0,-2,-1,1,2};
	int [] num1 = {-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6};
	ThreeSum ts = new ThreeSum();
	ArrayList<ArrayList<Integer>> aali = ts.threeSum(num1);
	ts.printf(aali);
	
	}

}
