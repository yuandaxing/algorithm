import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;
import java.util.StringTokenizer;

/*
ID: mryuan01
LANG: JAVA
TASK: milk3
*/

public class milk3 {


	public static class  MStat{

		@Override
		public int hashCode() {
			final int prime = 31;
			int result = 1;
			result = prime * limit[0] + limit[1];
			return result;
		}
		@Override
		public boolean equals(Object obj) {
			if (this == obj)
				return true;
			if (obj == null)
				return false;
			if (getClass() != obj.getClass())
				return false;
			MStat m = (MStat) obj;
			return stat[0] == m.stat[0] && stat[1] == m.stat[1];
		}

		int [] stat = null;
		public MStat(int c){
			stat = new int[3];
			stat[2] = c;
			stat[0] = 0;
			stat[1] = 0;
		}
		public MStat(int[] s){
			stat = s;
		}
		public MStat  X1ToX2(int x1, int x2){
			int left2 = limit[x2] - stat[x2];
			int[] a= new int [3];
			for(int i = 0; i< 3; i++){
				a[i] = stat[i];
			}
			if(stat[x1] > left2){ //pour x2 to full
				a[x1] -= left2;
				a[x2] += left2;
			}else{ //pour x1 into x2
				a[x2] += a[x1];
				a[x1] = 0;
			}
			
			return new MStat(a);
		}
		
		public boolean canX1pourX2(int x1, int x2){
			if(stat[x1] == 0 || stat[x2] == limit[x2])
				return false;
			else
				return true;
		}
		
		
		
	}
	
	public static int[] limit = new int[3];
	public static HashSet<MStat> hm = new HashSet<MStat>();
	/**
	 * @param args
	 * @throws IOException 
	 */
	static int getUnRevolve(int x1, int x2){
		if(x1 != 0  && x2 != 0)
			return 0;
		if(x1 != 1  && x2 != 1)
			return 1;
		return 2;
		
	}
	static void solve(MStat cur, int x1, int x2){
		MStat next = null;
		if(cur.canX1pourX2(x1, x2)){
			next = cur.X1ToX2(x1, x2);
			if(hm.contains(next))
				return ;
			hm.add(next);
			
			int x3 = getUnRevolve(x1, x2);
			
			solve(next, x1, x3);
			solve(next, x2, x3);
			solve(next, x2, x1);
			solve(next, x3, x1);
			solve(next, x3, x2);
		}
	}
	
	static ArrayList<Integer> collectOutput(){
		ArrayList<Integer> ai = new ArrayList<Integer>();
		HashSet<Integer> hs = new HashSet<Integer>();
		for(MStat m :hm){
			if(m.stat[0] == 0)
				hs.add(m.stat[2]);
		}
		for(Integer e : hs){
			ai.add(e);
		}
		return ai;
	}
	public static void main(String[] args) throws IOException {
		BufferedReader f = new BufferedReader(new FileReader("milk3.in"));
        // input file name goes above
		PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("milk3.out")));
		StringTokenizer st = new StringTokenizer(f.readLine().trim());
		limit[0] = Integer.parseInt(st.nextToken());
		limit[1] = Integer.parseInt(st.nextToken());
		limit[2] = Integer.parseInt(st.nextToken());
		
		MStat ms = new MStat(limit[2]);
		hm.add(ms);
		solve(ms, 2, 0);
		solve(ms, 2, 1);
		
		ArrayList<Integer> ret =  collectOutput();
		Collections.sort(ret);
		for(int i = 0; i < ret.size(); i++){
			if(i != 0)
				out.print(" ");
			out.print(ret.get(i).intValue());
		}
		out.println();
		out.close();
	}

}
