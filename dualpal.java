import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.StringTokenizer;

/*
ID: mryuan01
LANG: JAVA
TASK: dualpal
*/


public class dualpal {
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
	
	public static int[] getdualpal(int num, int least){

		int count = 0;
		int [] ret = new int[num];
		int j;
		int basePalCount;
		for(int i = least + 1; i < Integer.MAX_VALUE; i++){
			basePalCount = 0;
			for(j = 2; j <= 10; j++ ){
				if(isPalindromic(i, j) && ++basePalCount >= 2)
					break;
			}
			
			if(j <= 10){
				ret[count++] = i;
				if(count == num)
					return ret;
			}
		}
		return null;
	}
	
	public static void main(String[]args) throws IOException{
		BufferedReader f = new BufferedReader(new FileReader("dualpal.in"));
        // input file name goes above
		PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("dualpal.out")));
// Use StringTokenizer vs. readLine/split -- lots faster
		StringTokenizer st = new StringTokenizer(f.readLine().trim());
		int num = Integer.parseInt(st.nextToken());
		int least =  Integer.parseInt(st.nextToken());
		
		int[] res = getdualpal(num, least);
		for(int i = 0; i < num; i++){
			out.println(res[i]);
		}
		out.close();
	}
}
