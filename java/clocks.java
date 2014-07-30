import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.StringTokenizer;


/*
ID: mryuan01
LANG: JAVA
TASK: clocks
*/
public class clocks {
	public static String[] turn = {"", "ABDE", "ABC" , "BCEF","ADG",
		"BDEFH","CFI","DEGH","GHI","EFHI"};
	public static int[][] ct = null;
	static{
		ct = new int[10][];
		ct[0] = null;
		for(int i = 1; i <= 9; i++){
			ct[i] = new int[turn[i].length()];
			for(int j = 0; j < turn[i].length(); j++){
				ct[i][j] = turn[i].charAt(j) - 'A';
			}
		}
	}
	
	public static class clockM{
		int[][] clocks = null;
		HashSet<Integer> hs = new HashSet<Integer>();
		public clockM(int[][] m){
			clocks = m;
		}
		public clockM(){};
	
		public boolean isGoal(){
			for(int i = 0; i < 3; i++){
				for(int j = 0; j < 3; j++){
					if(clocks[i][j]  != 12)
						return false;
				}
			}
			return true;
		}
		
		int getVal(){
			int m = 0;
			for(int i = 0; i < 3; i++){
				for(int j = 0; j < 3; j++){
					m = m * 5 + clocks[i][j] / 3;
				}
			}
			return m;
		}
		public void applyK(int k){
			assert(k >= 1 && k<= 9);
			int s1 = 0, s2 = 0;
			for(int i = 0; i < ct[k].length; i++){
				s1 = ct[k][i] / 3;
				s2 = ct[k][i] % 3;
				clocks[s1][s2] += 3;
				if(clocks[s1][s2] > 12){
					clocks[s1][s2] %= 12;
				}
			}
	
		}
		
		public void unApplyK(int k){
			assert(k >= 1 && k<= 9);
			int s1 = 0, s2 = 0;
			for(int i = 0; i < ct[k].length; i++){
				s1 = ct[k][i] / 3;
				s2 = ct[k][i] % 3;
				clocks[s1][s2] -= 3;
				if(clocks[s1][s2] == 0){
					clocks[s1][s2]  = 12;
				}
			}
		}
		
	}


	
	public static class StepTrace{
		int [] step = null;
		int count = 0;
		public StepTrace(){
			step = new int[10];
			for(int i = 0; i < 10; i++){
				step[i] = 0;
			}
		}
		
		boolean canApplyK(int k){
			assert(k >= 1 && k <= 9);
			return step[k] < 3;
		}
		void applyK(int k){
			step[k]++;
			count++;
		}
		void unApplyK(int k){
			step[k]--;
			count--;
		}
		public int getstepn(){
			return count--;
		}
			
	}
	
	
	
	//this is 
	public static boolean canApplyAndApplyK(int k){
		if(!st.canApplyK(k))
			return false;
		
		src.applyK(k);
		st.applyK(k);
		int m = src.getVal();
		Integer v = new Integer(m); 
		Integer count = trace.get(v);
		if(count != null && count.intValue() <= st.getstepn()){
			src.unApplyK(k);
			st.unApplyK(k);
			return false;
		}
		ai.add(new Integer(k));
		if(count == null || count.intValue() > st.getstepn())
		trace.put(v, st.getstepn());
		return true;
	}
	public static void  unApplyK(int k){
		src.unApplyK(k);
		st.unApplyK(k);
		ai.remove(ai.size() - 1);
	}
	public static ArrayList<Integer> ai = new ArrayList<Integer>();
	public static HashMap<Integer, Integer> trace = new HashMap<Integer, Integer>();
	public static clockM src = null;
	public static StepTrace st = new StepTrace();
	public static boolean solve(int start, int n){
		if(start == n){
			if(src.isGoal())
				return true;
			
			return false;
		}
		
		for(int i = 1; i <= 9; i++){
			if(canApplyAndApplyK(i)){
				if(solve(start+1, n))
					return true;
				unApplyK(i);
			}
		}
		return false;
	}
	
	public static void main(String[]args) throws IOException{
		BufferedReader f = new BufferedReader(new FileReader("clocks.in"));
        // input file name goes above
		PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("clocks.out")));
		int[][] cl = new int[3][];
		for(int i = 0; i < 3; i++){
			cl[i] = new int[3];
			StringTokenizer st = new StringTokenizer(f.readLine());
			cl[i][0] = Integer.parseInt(st.nextToken());
			cl[i][1] = Integer.parseInt(st.nextToken());
			cl[i][2] = Integer.parseInt(st.nextToken());
		}
		
		src = new clockM(cl);
		int step = 1;
		while(!solve(0, step)){
		//	trace.clear();
			step++;
			//System.out.println(step);
		}
		
		for(int i = 0; i < ai.size(); i++){
			if(i != 0)
				out.print(" ");
			out.print(ai.get(i).intValue());
		}
		out.println();
		out.close();
	}

}
