

/*
ID: mryuan01
LANG: JAVA
TASK: milk2
*/
import java.io.*;
import java.util.*;

class milk2 {
	static public class Val implements Comparable<Val>{
		boolean right;
		int val;
		
		public Val(int val, boolean right){
			this.val = val;
			this.right = right;
		}
		public int compareTo(Val o) {
			// TODO Auto-generated method stub
			int d = this.val - o.val;
			if(d != 0)
				return d;
			if(!this.right)
				return -1;
			else if(!o.right)
				return 1;
			
			return 0;
		}
	}
	static public int [] longestIdleMilk(Val[] points){
		Arrays.sort(points);
		int startMilk = 0;
		int maxIdle = 0, maxMilk = 0;
		int startIdle = 0;
		boolean idle = true;
		boolean first = true;
		int count = 0;
		for(Val v : points){
			if(idle){
				assert (v.right == false);
				count++;
				idle = !idle;
				int idletime = v.val - startIdle;
				if(maxIdle < idletime){
					maxIdle = idletime;
				}
				if(first){
					first = !first;
					maxIdle = 0;
				}
				startMilk = v.val;
			}else{
				
				if(v.right) 
					count--;
				else
					count++;
				
				if(count == 0){
					idle = true;
					startIdle = v.val;
				}
				
				int busyTime = v.val - startMilk;
				if(maxMilk < busyTime)
					maxMilk = busyTime;
				
				}
			}
		
		int [] ret = new int[2];
		ret[0] = maxIdle;
		ret[1] = maxMilk;
		return ret;
		
		}
		
  public static void main (String [] args) throws IOException {
    // Use BufferedReader rather than RandomAccessFile; it's much faster
    BufferedReader f = new BufferedReader(new FileReader("milk2.in"));
                                                  // input file name goes above
    PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("milk2.out")));
    // Use StringTokenizer vs. readLine/split -- lots faster
    String s = f.readLine();
    int  num = Integer.parseInt(s.trim());
    Val[] points = new Val[num * 2 ];
    
    for(int i = 0; i < num; i++){
    	StringTokenizer st = new StringTokenizer(f.readLine());
						  // Get line, break into tokens
    	int i1 = Integer.parseInt(st.nextToken());    // first integer
    	int i2 = Integer.parseInt(st.nextToken());    // second integer
    	points[2 * i] = new Val(i1, false);
    	points[2 * i + 1] = new Val(i2, true);
    }
    // output result
    int[] ret =   longestIdleMilk(points);
    out.println(ret[1] + " " + ret[0]);
    out.close();                                  // close the output file
    System.exit(0);                               // don't omit this!
  }
}

