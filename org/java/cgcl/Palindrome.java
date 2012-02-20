package org.java.cgcl;

public class Palindrome {
	public  static boolean test1palindrome(int x){
		int inte = x;
		int save = inte;	
		int reverse = 0;
		if(inte < 0)
			return false;
		while(inte != 0){
				int tail =  inte % 10;
				reverse = reverse * 10 + tail;
				inte /= 10;
			}
		
		if(reverse == save){
			return true;
		}else{
			return false;
		}
	}
	
	public  static boolean test2palindrome(int inte){
		if(inte < 0){
			return false;
		}
		int k = 1;
		while(inte / k > 10){
			k *= 10;
		}
		int left = k;
		int right = 10;
		int right_right = 1;
		while(left > right_right){
			int first = (inte / left) % 10;
			int end = (inte % right) / right_right;
			if(first != end){
				return false;
			}
			left /= 10;
			right *= 10;
			right_right *= 10;
		}
		return true;
	}
	static boolean isPalindrome(int x) {
		  if (x < 0) return false;
		  int div = 1;
		  while (x / div >= 10) {
		    div *= 10;
		  }
		  while (x != 0) {
		    int l = x / div;
		    int r = x % 10;
		    if (l != r) return false;
		    x = (x % div) / 10;
		    div /= 100;
		  }
		  return true;
		}

	
	public static void main(String[] args){
		int a = 12321;
		int b = 1;
		int c = 0;
		int d = -1;
		int e = 123;
		int f = 210;
		
		assert(test1palindrome(a));
		assert(test1palindrome(b));
		assert(test1palindrome(c));
		assert(test1palindrome(d) == false);
		assert(test1palindrome(e) == false);
		assert(test1palindrome(f) == false);
		
		//assert(test2palindrome)
		assert(test2palindrome(a));
		assert(test2palindrome(b));
		assert(test2palindrome(c));
		assert(test2palindrome(d) == false);
		assert(test2palindrome(e) == false);
		assert(test2palindrome(f) == false);
		assert(test2palindrome(101001) == false);
		assert(isPalindrome(101111) == false);
	}

}
