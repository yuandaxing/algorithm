package org.java.cgcl;

import java.util.BitSet;

public class LongSubStringWORCharacter {
	public static BitSet bs = new BitSet(256);
	static boolean checkNoRepeat(String s){
		bs.clear();
		for(int i = 0; i < s.length(); i++){
			if(bs.get(s.charAt(i)))
				return false;
			else
				bs.set(s.charAt(i));
		}
		return true;
	}
	
	static int bruteLSSWORC(String s){
		int max = 0;
		for(int i = 0; i < s.length(); i++){
			for(int j = i; j < s.length(); j++){
				if(max < j + 1 - i &&  checkNoRepeat(s.substring(i, j+1)))
					max = j  +  1 - i; 
			}
		}
		return max;
	}
	
	static int bestLSSWORC(String s){
		bs.clear();
		int max = 0;
		for(int i = 0, j = 0; i < s.length(); i++){
			if(bs.get(s.charAt(i))){
				while(s.charAt(j) != s.charAt(i)){
					bs.clear(s.charAt(j));
					j++;
				}
				bs.clear(j);
				j++;
			}else{
				if(max < i - j + 1)
					max = i + 1 - j;
				bs.set(s.charAt(i));
			}
		}
		return max;
	}
	
	
	public static void main(String[] args){
		assert(bruteLSSWORC("bbbbbbbbbbbb") == 1);
		assert(bruteLSSWORC("abcabcbb") == 3);
		assert(bestLSSWORC("bbbbbbbbbbbb") == 1);
		assert(bestLSSWORC("abcabcbb") == 3);
	}

}
