package org.java.cgcl;

public class ContainerMostWater {

	int min(int a, int b){
		return a > b ? b : a;
	}
    public int maxArea(int[] height) {
        // Start typing your Java solution below
        // DO NOT write main() function
    	assert(height.length > 1);
    	int max = Integer.MIN_VALUE;
    	for(int i = 0; i < height.length - 1; i++){
    		for(int j = i+1 ; j < height.length; j++){
    			int area = (j - i) * min(height[i], height[j]);
    			if(area > max)
    				max = area;
    		}
    	}
        return max;
    }
}
