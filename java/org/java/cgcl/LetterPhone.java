package org.java.cgcl;

import java.util.ArrayList;

public class LetterPhone {

	String[] table = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
	/**
	 * @param args
	 */
    public ArrayList<String> letterCombinations(String digits) {
        // Start typing your Java solution below
        // DO NOT write main() function
    	ArrayList<String> als = new ArrayList<String>();
    	if(digits.length() == 0){
    		als.add("");
    		return als;
    	}
    	if(digits.length() == 1){
    		String s = table[digits.charAt(0) - '0'];
    		for(int i = 0; i < s.length(); i++){
    			als.add(s.substring(i, i+1));
    		}
    		return als;
    	}
    	
    	ArrayList<String> post = letterCombinations(digits.substring(1));
    	
    	String ss = table[digits.charAt(0) - '0'];
    	if(ss.length() == 0){
    		als.addAll(post);
    	}else{
    		
    		if(post.size() == 0){
        		for(int i = 0; i < ss.length(); i++){
        			als.add(ss.substring(i, i+1));
        		}
    		}else{
    		
    			for(int i = 0; i < ss.length() ; i++){
    				for(String str : post){
    					als.add(ss.substring(i, i+1) + str);
    				}
    			}
    		}
    	}
    	return als;
    }
    
    public void printf(ArrayList<String> al){
    	System.out.println(al.size());
    	for(String s : al)
    		System.out.println(s);
    }
    
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		LetterPhone lp = new LetterPhone();
		lp.printf(lp.letterCombinations("23"));
	}

}
