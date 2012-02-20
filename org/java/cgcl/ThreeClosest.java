package org.java.cgcl;

import java.util.Arrays;

public class ThreeClosest {

	private int diff(int a, int b){
		return a > b ?  a - b : b - a; 
	}
    public int threeSumClosest(int[] num, int target) {
        // Start typing your Java solution below
        // DO NOT write main() function
    	int dis = Integer.MAX_VALUE;
    	int save = 0;
    	Arrays.sort(num);
    	
    	for(int i = 0; i < num.length - 2; i++){
    		for(int j = i+1; j < num.length - 1; j++){
    			for(int k = j + 1; k < num.length; k++){
    				int sum = num[i] + num[j] + num[k];
    				int d = diff(target, sum);
    				if(d < dis){
    					dis = d;
    					save = sum;
    				}
    				if(sum >=  target) break;
    			}
    		}
    	}
    	
    	return save;
    }
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ThreeClosest tc = new ThreeClosest();
		int [] num = {-1, 2, 1, -4};
		System.out.print(tc.threeSumClosest(num, 1));
	}

}
