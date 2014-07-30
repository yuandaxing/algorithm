package org.java.cgcl;

public class StrStr {
    public String strStr(String haystack, String needle) {
        // Start typing your Java solution below
        // DO NOT write main() function
    	assert(haystack != null && needle != null);
        if(needle.length() == 0)
        	return haystack;
        if(haystack.length() == 0)
        	return null;
        int i, j;
    	for(i = 0; i <= haystack.length() - needle.length(); i++){
    		for( j = 0; j < needle.length(); j++){
    			if(haystack.charAt(i+j) != needle.charAt(j))
    				break;
    		}
    		if(j >= needle.length())
    			return haystack.substring(i);
    	}
    	return null;
    }
    
    public static void main(String[] args){
    	StrStr st = new StrStr();
    	System.out.println(st.strStr("aaba", "ab"));
    }
}
