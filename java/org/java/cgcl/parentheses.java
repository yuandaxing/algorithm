package org.java.cgcl;

import java.util.ArrayList;
import java.util.HashMap;

public class parentheses {
	public HashMap<Integer, ArrayList<String>> lookTable = 
			new HashMap<Integer, ArrayList<String>>();

	public ArrayList<String> getP(int n){
		ArrayList<String> als = new ArrayList<String>();
		
		if(n == 0)
			return als;
		if(n == 1){
			als.add(new String("()"));
			return als;
		}
		ArrayList<String> lt = lookTable.get(new Integer(n));
		if(lt != null)
			return lt;
		
		for(int i = 1; i <= n; i++){
			ArrayList<String> pre = getP(i - 1);
			ArrayList<String> post = getP(n - i);
			ArrayList<String> tmp = new ArrayList<String> ();
			if(pre.size() == 0){
					tmp.add(new String("()"));
			}else{
				for(String sb : pre){
					tmp.add(new String("("+sb.toString()+")"));
				}
			}
			
			if(post.size() == 0){
				als.addAll(tmp);
			}else{
				for(String sb1 : tmp){
					for(String sb2 : post){
						als.add(sb1 + sb2);
					}
				}
			}		
		}
		
		
		lookTable.put(new Integer(n), als);
		return als;	
	}
	
    public ArrayList<String> generateParenthesis(int n) {
        // Start typing your Java solution below
        // DO NOT write main() function
       
        return getP(n);
    }
    public void printf(ArrayList<String> al){
    	System.out.println(al.size());
    	for(String s : al)
    		System.out.println(s);
    }
    public static void main(String[] args){
    	
    	parentheses par= new parentheses();
    	par.printf(par.generateParenthesis(6));
    	
    }
}
