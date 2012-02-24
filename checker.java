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
TASK: checker
*/
public class checker {

	public static int N = 0;
	public static int[] rowholder = null;
	public static BitSet colp = null;
	public static BitSet triangle_rd = null;  //  i - j + N;
	public static BitSet triangle_ld = null; // i + j
	
	static boolean canGo(int row, int col){
		if(colp.get(col))
			return false;
		if(triangle_rd.get(row - col + N))
			return false;
		if(triangle_ld.get(row + col))
			return false;
		return true;
	}
	static void go(int row, int col){
		rowholder[row] = col;
		colp.set(col);
		triangle_rd.set(row - col + N);
		triangle_ld.set(row + col);
	}
	static void unGo(int row, int col){
		colp.clear(col);
		triangle_rd.clear(row - col + N);
		triangle_ld.clear(row + col);
	}

	private static int count = 0;
	static void solve(int row){
		if(row == N){
			if(count < 3){
				for(int i = 0; i < N; i++){
					if(i != 0)
						out.print(" ");
					out.print(rowholder[i] + 1);
				}
				out.println();
			}
			count++;
			return ;
		}
		for(int i = 0; i < N; i++){
			if(canGo(row, i)){
				go(row, i);
				solve(row + 1);
				unGo(row, i);
			}
		}
	}
	static PrintWriter out = null;
	public static void main(String[] args) throws IOException {
		BufferedReader f = new BufferedReader(new FileReader("checker.in"));
        // input file name goes above
		out = new PrintWriter(new BufferedWriter(new FileWriter("checker.out")));
		N = Integer.parseInt(f.readLine().trim());
		rowholder = new int[N];
		colp = new BitSet(N);
		colp.clear();
		triangle_rd = new BitSet(2 * N);
		triangle_rd.clear();
		triangle_ld = new BitSet(2 * N);
		triangle_ld.clear();
		solve(0);
		out.println(count);
		out.close();
	}
	
}
