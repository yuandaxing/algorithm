package org.java.cgcl;

public class LongestCommonPrefix {
    public String longestCommonPrefix(String[] strs) {
        // Start typing your Java solution below
        // DO NOT write main() function
    	if(strs.length == 0)
    		return "";
    	
    	String lcp = strs[0];
    	for(String str :  strs){
    		if(lcp.equals(""))
    			return lcp;
    		int j;
    		for(j = 0; j < str.length() && j < lcp.length(); j++){
    			if(lcp.charAt(j) != str.charAt(j)){
    				lcp = lcp.substring(0, j);
    				break;
    			}
    		}
    		if(j >= str.length() || j >= lcp.length()){
    			lcp = lcp.substring(0, j);
    		}
    	}
        return lcp;
    }
    
    public static void main(String[] args){
    	String[] strs = {"flower","flow","flight"};
    	LongestCommonPrefix lcp = new LongestCommonPrefix();
    	System.out.println(lcp.longestCommonPrefix(strs));
    }

}
