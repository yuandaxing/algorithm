import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.StringTokenizer;


/*
ID: mryuan01
LANG: JAVA
TASK: sprime
*/
public class sprime {
	public static int N = 0;
	public static int[] cand = {1, 2, 3, 5, 7, 9};
	private static ArrayList<Integer> ai = new ArrayList<Integer>();
	
	public static int[] prime = null;
	public static int pos = 0;
	static void compute(int max){
		prime[pos++] = 2;
		int endb = (int) Math.sqrt(max) + 1;
		for(int i = 3; i <= endb; i++){
			int end = (int )Math.sqrt(i) + 1;
			for(int j = 0; j < pos ; j++){
				if(i % prime[j] == 0)
					break;
				if(prime[j] >= end){
					prime[pos++] = i;
					break;
				}
			}
		}
	}
	static boolean isPrime(int begin){

		if(begin == 1)
			return false;
		if(begin == 2)
			return true;
		int end = (int )Math.sqrt(begin) + 1;
		boolean isprime = false;
		int j;
		for(j = 0; j < pos ; j++){
			if(begin % prime[j] == 0)
				break;
			if(prime[j] >= end){
				isprime = true;
				break;
			}
		}
		if(isprime || j >= pos)
			return true;
		
		return false;
}
	
	public static void solve(int start, int val){
		if(start >= N){
			int save = val;
			for(int i = 0; i < N ; i++){
				if(!isPrime(val))
					return ;
				val /= 10;
			}
			ai.add(save);
			return ;
		}
		
		for(int i = 0; i  < cand.length; i++){
			if(start == 0 && i == 0) // 1 cannot be the first
				continue;
			if(i == 1 && start != 0) //2 can only be the first
				continue;
			solve(start + 1, val * 10 + cand[i]);
		}
		
	}
	public static void main(String[] args) throws IOException {
		BufferedReader f = new BufferedReader(new FileReader("sprime.in"));
        // input file name goes above
		PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("sprime.out")));
		N = Integer.parseInt(f.readLine().trim());
		int max = (int)Math.pow(10, N);
		int len  = (int) Math.sqrt(max) + 1;
		prime = new int[len];
		compute(max);
		solve(0, 0);
		
		for(Integer e : ai){
			out.println(e);
		}
		
		out.close();
		
	}
}
