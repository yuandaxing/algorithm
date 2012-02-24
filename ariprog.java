import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.BitSet;
import java.util.Collections;

/*
ID: mryuan01
LANG: JAVA
TASK: ariprog
*/
public class ariprog {

	private static BitSet bs = null;
	private static int[] nums = null;
	private static int N = 0;
	private static  int M = 0;
	private static ArrayList<Pair>ap = new ArrayList<Pair>();
	
	public static class Pair implements Comparable<Pair>{
		public int start;
		public int d;
		public Pair(int start, int d){
			this.start = start;
			this.d = d;
		}
		@Override
		public int compareTo(Pair arg0) {
			// TODO Auto-generated method stub
			int di = d - arg0.d;
			return di != 0 ?  di : (start - arg0.start);
		}
	}
	
	public static void solve(){
		int d;
		int k;
		for(int i = 0; i < nums.length - 1; i++){
			for(int j = i+1; j < nums.length; j++){
				d = nums[j] - nums[i];
				
				if(nums[i] + (N  - 1)* d> nums[nums.length - 1])
					break;
				for(k= 2; k < N; k++){
					if(!bs.get(nums[i] + d * k))
						break;
				}
				if(k >= N)
					ap.add(new Pair(nums[i], d));
			}
		}
	}
	
	public static void init()
	{
		int total = 2 * M * M ;
		bs = new BitSet(total+1);
		for(int p = 0; p <= M; p++ ){
			for(int q = 0; q <= p; q++){
				bs.set(p*p + q*q);
			}
		}
		
		int len = 0;
		for(int i = 0; i<= total; i++){
			if(bs.get(i))
				len++;
		}
		
		nums = new int[len];
		int begin = 0;
		for(int i = 0; i<= total; i++){
			if(bs.get(i))
				nums[begin++] = i;
		}
	}
	/**
	 * @param args
	 * @throws IOException 
	 */
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader f = new BufferedReader(new FileReader("ariprog.in"));
        // input file name goes above
		PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("ariprog.out")));
		N = Integer.parseInt(f.readLine().trim());
		M = Integer.parseInt(f.readLine().trim());
		init();
		solve();
		if(ap.isEmpty()){
			out.println("NONE");
		}else{
			Collections.sort(ap);
			for(Pair p: ap){
				out.println(p.start + " " + p.d);
			}
		}
			
		out.close();
	}

}
