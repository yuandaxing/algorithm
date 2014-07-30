import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

/*
ID: mryuan01
LANG: JAVA
TASK: numtri
*/
public class numtri {
	public static int[][]  numT = null;
	public static int[][]  result = null;

	public static void dp(){
		for(int i = 0; i < numT.length; i++){
			for(int j = 0; j < numT[i].length; j++){
				int max = Integer.MIN_VALUE;
				if(i - 1 < 0){
					max = 0;
				}else if(j - 1 < 0){
					max = result[i - 1][j];
				}else if(j > i - 1){
					max = result[i - 1][j - 1];
				}else{
					if(result[i - 1][j] > result[i - 1][j - 1])
						max = result[i - 1][j];
					else
						max = result[i - 1][j - 1];
				}
				result[i][j] = numT[i][j] + max;
			}
		}
	}
	static int collectOutput(){
		int max = Integer.MIN_VALUE;
		for(int i = 0; i < result[result.length - 1].length; i++){
			if(max < result[result.length - 1][i])
				max = result[result.length - 1][i];
		}
		return max;
	}
	public static void main(String[] args) throws IOException {
		BufferedReader f = new BufferedReader(new FileReader("numtri.in"));
        // input file name goes above
		PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("numtri.out")));
		
		int len = Integer.parseInt(f.readLine().trim());
		numT = new int[len][];
		result = new int[len][];
		for(int i = 0; i < len; i++){
			numT[i] = new int[i+1];
			result[i] = new int[i+1];
			StringTokenizer st = new StringTokenizer(f.readLine().trim());
			for(int j = 0; j <= i; j++){
				numT[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		

		dp();
		int  ret =  collectOutput();
		
		out.println(ret);
		out.close();
	}
}
