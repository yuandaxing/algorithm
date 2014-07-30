import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.StringTokenizer;

/*
ID: mryuan01
LANG: JAVA
TASK: pprime
*/
public class pprime {
	public static int a = 0;
	public static int b = 0;
	public static int na = 0;
	public static int nb = 0;
	public static int pos = 0;
	public static int[] prime = null;
	public static HashSet<Integer> pp = new HashSet<Integer>();
	
	static boolean isPalindrome(int i){
		int k = 1;
		while(k <= i / 10){
			k *= 10;
		}
		
		while(i != 0){
			int left = i / k;
			int right = i % 10;
			if(left != right)
				return false;
			i = i % k / 10;
			k = k / 100;
		}
		return true;
		
	}
	static boolean isPrime(int begin){

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
	static void compute(){
		prime[pos++] = 2;
		int endb = (int) Math.sqrt(b) + 1;
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
	public static void solve(int rh, int rl,  int val){
		if(rh < rl){
			if(val < a || val > b)
				return ;
			if(isPrime(val))
				pp.add(val);
			
			
			return ;
		}
		if(rh == rl){
			int expand = (int)Math.pow(10, rh - 1);
			for(int i = 0; i < 10; i++){
				solve(rh - 1, rl + 1, val + expand * i);
			}
		}else{
			int he = (int)Math.pow(10, rh - 1);
			int le = (int)Math.pow(10, rl - 1);
			for(int i = 0; i< 10; i++){
				solve(rh - 1, rl + 1, val + he * i + le * i);
			}
		}
		
	}
	public static int  getNumCount(int nu){
		int count = 0;
		while(nu != 0){
			count++;
			nu /= 10;
		}
		return count;
	}
	public static void main(String[] args) throws IOException {
		BufferedReader f = new BufferedReader(new FileReader("pprime.in"));
        // input file name goes above
		PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("pprime.out")));
		StringTokenizer st = new StringTokenizer(f.readLine().trim());
		a = Integer.parseInt(st.nextToken());
		b = Integer.parseInt(st.nextToken());
		na = getNumCount(a);
		nb = getNumCount(b);
		int size =(int) Math.sqrt(b) + 10;
		prime = new int[ size];
		compute();
		for(int i = na; i <= nb; i++){
			solve(i, 1, 0);
		}
		ArrayList<Integer> ai = new ArrayList<Integer> ();
		ai.addAll(pp);
		Collections.sort(ai);
		for(Integer e : ai){
			out.println(e);
		}
		out.close();
	}
}
