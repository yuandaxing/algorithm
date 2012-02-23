import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.HashSet;
import java.util.StringTokenizer;


/*
ID: mryuan01
LANG: JAVA
TASK: clocks
*/

 class clocks2 {

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
		public clockM(int[][] m){
			clocks = m;
		}
		public clockM(){
			clocks = new int [3][];
			for(int i = 0; i < 3; i++){
				clocks[i] = new int[3];
			}	
		}
		public clockM copy(clockM cm){
			for(int i = 0; i< 3; i++){
				for(int j = 0; j < 3; j++){
					clocks[i][j] = cm.clocks[i][j]; 
				}
			}
			return this;
		}
	
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
	public static int getStep(){
		int count = 0;
		for(int i = 1; i<= 9; i++){
			count+= step[i];
		}
		return count;
	}
	
	public static void  collectAndAssert(){
		check.copy(src);
		for(int i = 1; i <= 9; i++){
			for(int j = 0; j< step[i]; j++){
				check.applyK(i);
			}
		}
		int count;
		if(check.isGoal() && (count = getStep()) < min ){
			min = count;
			for(int i = 1; i <= 9; i++){
				fin[i] = step[i];
			}
		}
	}
	
	public static clockM src = null;
	public static clockM check = new clockM();
	static int [] step = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
	static int min = Integer.MAX_VALUE;
	static int[] fin = new int[10];
	public static void solve(int start){
		if(start > 9){
			collectAndAssert();
			return ;
		}
		for(int i = 0; i<= 3; i++){
			step[start] = i;
			solve(start + 1);
		}
	}
	public static int init = 0;
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
		solve(1);
		boolean notfirst = false;
		for(int i = 1; i<= 9; i++){
			for(int j = 0; j< fin[i]; j++){
				if(notfirst)
					out.print(" ");
				out.print(i);
				notfirst =true;
			}
		}
		out.println();
		out.close();
	}
}

 
 
