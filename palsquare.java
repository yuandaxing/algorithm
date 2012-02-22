import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;


/*
ID: mryuan01
LANG: JAVA
TASK: palsquare
*/
public class palsquare {
	
	public static final String num="0123456789ABCDEFGHIGK";
	public static boolean isPalindromic(int num, int base){
		int save = 1;
		while(save <= num / base){
			save *= base;
		}
		while(num != 0){
			int first = num / save;
			int last = num % base;
			if(first != last)
				return false;
			num = (num % save) / base;
			save = save / base / base;
		}
		return true;
	}
	
	public static String getPalindromicBase(int nu, int base, boolean pal){
		StringBuffer sb = new StringBuffer();
		while(nu != 0){
			int left = nu % base;
			sb.append(num.charAt(left));
			nu /= base;
		}
		if(!pal)
			return sb.reverse().toString();
		else
			return sb.toString();
	}
	
	
	public static void main(String[]args) throws IOException{
		BufferedReader f = new BufferedReader(new FileReader("palsquare.in"));
        // input file name goes above
		PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("palsquare.out")));
// Use StringTokenizer vs. readLine/split -- lots faster
		int base  = Integer.parseInt(f.readLine().trim());
		
		for(int i = 1; i <= 300; i++){
			int square = i*i;
			if(isPalindromic(square, base)){
				out.print(getPalindromicBase(i, base, false));
				out.println(" " + getPalindromicBase(square, base, true));
			}
		}
		out.close();
	}

}
