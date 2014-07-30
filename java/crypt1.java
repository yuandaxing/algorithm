import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.BitSet;
import java.util.StringTokenizer;

/*
ID: mryuan01
LANG: JAVA
TASK: crypt1
*/
public class crypt1 {
	private static BitSet bs = new BitSet(10);
	private static int[] nums = null;
	static{
		bs.clear();
	}
	private static int numSolve = 0;

	public static boolean numInRight(int num, int digits){
		if(digits < 2 || digits > 4)
			return false;
		if(digits == 2 && (num < 10 || num >= 100))
			return false;
		if(digits == 3 && (num < 100 || num >= 1000))
			return false;
		if(digits == 4 && (num < 1000 || num >= 10000))
			return false;
		int k = 0;
		while(num != 0){
			k = num % 10;
			if(bs.get(k) == false)
				return false;
			num /= 10;
		}
		return true;
	}
	public static void getM2(int start, int M1, int M2){
		if(start >= 2){
			if(numInRight(M2, 2) && numInRight(M1 * M2, 4))
				numSolve++;
			return ;
		}
		for(int i = 0; i < nums.length; i++){
			if(numInRight(M1 * nums[i], 3)){
				getM2(start+1, M1, M2 * 10 + nums[i]);
			}
		}
	}
	public static void getM1(int start, int M1){
		if(start >= 3){
			if(numInRight(M1, 3))
				getM2(0, M1, 0);
			return ;
		}
		for(int i = 0; i < nums.length; i++){
			getM1(start+1, M1 * 10 + nums[i]);
		}
	}
	
	public static void main(String[]args) throws IOException{
		BufferedReader f = new BufferedReader(new FileReader("crypt1.in"));
        // input file name goes above
		PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("crypt1.out")));
		int num = Integer.parseInt(f.readLine().trim());
		nums = new int[num];
		StringTokenizer st = new StringTokenizer(f.readLine());
		for(int i = 0; i < num; i++){
			nums[i] = Integer.parseInt(st.nextToken());
			bs.set(nums[i]);
		}
		getM1(0, 0);
		out.println(numSolve);
		out.close();
	}

}

