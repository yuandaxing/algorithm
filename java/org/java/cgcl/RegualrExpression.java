package org.java.cgcl;

public class RegualrExpression {
    public boolean isMatch(String s, String p) {
        // Start typing your Java solution below
        // DO NOT write main() function
    	if(s.equals("") && p.equals("")){
    		return true;
    	}else if(p.length() == 0){
    		return false;
    	}else if(p.charAt(0) == '.'){
    		if(p.length() > 1 && p.charAt(1) == '*'){
    				for(int i = 0; i <= s.length(); i++){
    					if(isMatch(s.substring(i), p.substring(2)))
    							return true;
    				}
    		}else{
    			if(s.length() > 0 && isMatch(s.substring(1), p.substring(1))){
    				return true;
    			}
    		}
    		return false;
    	}else {
    		if(p.length() > 1 && p.charAt(1) == '*'){
    			if(isMatch(s.substring(0), p.substring(2)))
    				return true;
    			for(int i = 0; i < s.length(); i++){
    				if(s.charAt(i) == p.charAt(0) && isMatch(s.substring(i+1), p.substring(2))){
    					return true;
    				}else if(s.charAt(i) != p.charAt(0)){
    					break;
    				}
    		}
    	}else{
    		if(s.length() > 0 && s.charAt(0) == p.charAt(0) && isMatch(s.substring(1), p.substring(1)))
    				return true;
    	}
    	return false;
    	}
    }
    
    public static void main(String[] args){
    	RegualrExpression re = new RegualrExpression();
    	assert(re.isMatch("aa", "a") == false);
    	assert(re.isMatch("aa", "aa"));
    	assert(re.isMatch("aaa", "aa") == false);
    	assert(re.isMatch("aa", "a*"));
    	assert(re.isMatch("aa", ".*"));
    	assert(re.isMatch("ab", ".*"));
    	assert(re.isMatch("aab", "c*a*b"));
    	assert(re.isMatch("abcbcd", "a.*c.*d"));
    	assert(re.isMatch("ababccbabababbbbc", ".*a*ba*.a*b*a*.*b.*"));
     	assert(re.isMatch("cbcbbbcbcbcbabcb", "b*b*ab*c*b*b*b*a*c*") == false);
    	System.out.append("complete");
    	
    }
}
