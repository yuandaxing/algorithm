import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

/*
ID: mryuan01
LANG: JAVA
TASK: barn1
*/
public class barn1 {

	public static int findMin(int[] cowOccupy, int M){
		int[] interval = new int[cowOccupy.length - 1];
		Arrays.sort(cowOccupy);
		int min = cowOccupy[cowOccupy.length - 1] - cowOccupy[0] + 1;
		for(int i = 0; i < cowOccupy.length - 1; i++){
			interval[i] = cowOccupy[i+1] - cowOccupy[i] - 1;
		}
		Arrays.sort(interval);
		M--;
		for(int j = interval.length - 1; j >= 0 && M > 0; j--, M--){
			if(interval[j] == 0)
				return min;
			min -= interval[j];
		}
		return min;
	}
	public static void main(String[]args) throws IOException{
		BufferedReader f = new BufferedReader(new FileReader("barn1.in"));
        // input file name goes above
		PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("barn1.out")));
// Use StringTokenizer vs. readLine/split -- lots faster
		StringTokenizer st = new StringTokenizer(f.readLine().trim());
		int M = Integer.parseInt(st.nextToken());
		int S =  Integer.parseInt(st.nextToken());
		int C = Integer.parseInt(st.nextToken());
		int[] cowOccupy = new int[C];
		for(int i = 0; i < C; i++ ){
			cowOccupy[i] = Integer.parseInt(f.readLine().trim());
		}
		out.println(findMin(cowOccupy, M));
		out.close();
	}
}
