import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayDeque;


/*
ID: mryuan01
LANG: JAVA
TASK: transform
*/
public class transform {
	public static final int MAX_STEP1 = 1;
	public static final int MAX_STEP2 = 1;
	public static final int MAX_STEP3 = 1;
	public static final int MAX_STEP4 = 1;
	public static final int MAX_STEP5 = 2;
	public static final int MAX_STEP6 = 1;
	public static class Stats{
		int[] pos = {0,0, 0, 0, 0, 0, 0};
		int step1 = 0;
		int step2 = 0;
		int step3 = 0;
		int step4 = 0;
		int step5 = 0;
		int step6 = 0;
		byte [][] matrix = null;
		public Stats(byte [][]matrix){
			this.matrix =matrix; 
		}
		public Stats(int size){
			matrix = new byte[size][];
			for(int i = 0; i < size; i++){
				matrix[i] = new byte[size];
			}
		}
		public int[] getPos(){
			int len = step1+step2+step3+step4+step5+step6;
			int [] ret = new int[len];
			for(int i = 0; i < len; i++){
				ret[i] = pos[i];
			}
			return ret;
		}
		public Stats setStep(int K){
			pos[step1+step2+step3+step4+step5+step6] = K;
			if(K == 1){
				step1++;
			}else if(K == 2){
				step2++;
			}else if(K == 3){
				step3++;
			}else if(K == 4){
				step4++;
			}else if(K == 5){
				step5++;
			}else if(K == 6){
				step6++;
			}
			return this;
		}
		public boolean canGoStepK(int K){
			assert(K >= 1 && K <= 5);
			if(K == 1){
				return step1 < MAX_STEP1;
			}else if(K == 2){
				 return step2 < MAX_STEP2;
			}else if(K == 3){
				return step3 < MAX_STEP3;
			}else if(K == 4){
				return step4 < MAX_STEP4;
			}else if(K == 5){
				return step5 < MAX_STEP5;
			}else{
				return step6 < MAX_STEP6;
			}
			
		}
		public boolean isSame(Stats s){
			for(int i = 0; i < matrix.length; i++){
				for(int j = 0; j < matrix.length; j++){
					if(matrix[i][j] != s.matrix[i][j])
						return false;
				}
			}
			return true;
		}
		
		private void stepCopy(Stats s1, Stats s2){
			s1.step1 = s2.step1;
			s1.step2 = s2.step2;
			s1.step3 = s2.step3;
			s1.step4 = s2.step4;
			s1.step5 = s2.step5;
			s1.step6 = s2.step6;
		}
		
		public Stats rotate90(){
			int len = matrix.length;
			Stats s1 = new Stats(matrix.length);
			for(int i = 0; i < matrix.length; i++){
				for(int j = 0; j < matrix.length; j++){
					s1.matrix[i][j] = matrix[len - j - 1][i];
				}
			}
			stepCopy(s1, this);
			return s1;
		}
		
		public Stats rotate180(){
			int len = matrix.length;
			Stats s1 = new Stats(matrix.length);
			for(int i = 0; i < matrix.length; i++){
				for(int j = 0; j < matrix.length; j++){
					s1.matrix[i][j] = matrix[len - i - 1][len - j - 1];
				}
			}
			stepCopy(s1, this);
			return s1;
		}
		public Stats rotate270(){
			int len = matrix.length;
			Stats s1 = new Stats(matrix.length);
			for(int i = 0; i < matrix.length; i++){
				for(int j = 0; j < matrix.length; j++){
					s1.matrix[i][j] = matrix[j][len - i - 1];
				}
			}
			stepCopy(s1, this);
			return s1;
		}
		
		public Stats mirror(){
			int len = matrix.length;
			Stats s1 = new Stats(matrix.length);
			for(int i = 0; i < matrix.length; i++){
				for(int j = 0; j < matrix.length; j++){
					s1.matrix[i][j] = matrix[i][len - j - 1];
				}
			}
			stepCopy(s1, this);
			return s1;
		}
		public Stats noChange(){
			Stats s1 = new Stats(matrix.length);
			for(int i = 0; i < matrix.length; i++){
				for(int j = 0; j < matrix.length; j++){
					s1.matrix[i][j] = matrix[i][j];
				}
			}
			stepCopy(s1, this);
			return s1;
		}
	}

	/**
	 * @param args
	 * @throws IOException 
	 */
	
	public static int[] CalculateMin(Stats src, Stats dest){
		ArrayDeque<Stats> stack = new ArrayDeque<Stats>();
		boolean first = true;
		stack.add(src);
		while(!stack.isEmpty()){
			Stats cur = stack.remove();
			if(first){
				first = !first;
			}else{
				if(cur.isSame(dest)){
					return cur.getPos();
				}
			}
			if(cur.canGoStepK(1)){
				stack.add(cur.rotate90().setStep(1));
			}
			if(cur.canGoStepK(2)){ 
				stack.add(cur.rotate180().setStep(2));
			}
			if(cur.canGoStepK(3)){
				stack.add(cur.rotate270().setStep(3));
			}
			if(cur.canGoStepK(4)){
				stack.add(cur.mirror().setStep(4));
			}
			if(cur.canGoStepK(5)){
				Stats mirror = cur.mirror();
				stack.add(mirror.rotate90().setStep(5));
				stack.add(mirror.rotate180().setStep(5));
				stack.add(mirror.rotate270().setStep(5));
			}
			if(cur.canGoStepK(6)){
				stack.add(cur.noChange().setStep(6));
			}
		}
		int [] last = {7};
		return last;
		
	}
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		 BufferedReader f = new BufferedReader(new FileReader("transform.in"));
         // input file name goes above
		 PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("transform.out")));
		 
		 String s = f.readLine();
		    int  num = Integer.parseInt(s.trim());
		    byte[][] src, dest;
		    src = new byte[num][];
		    dest = new byte[num][];
		    for(int i = 0; i < num ; i++){
		    	src[i]= f.readLine().trim().getBytes();
		    }
		    for(int i = 0; i < num; i++){
		    	dest[i] = f.readLine().trim().getBytes();
		    }
		    int [] step = CalculateMin(new Stats(src), new Stats(dest));
		    for(int i = 0; i < step.length; i++){
		    	if(i != 0)
		    		out.print(" ");
		    	out.print(step[i]);
		    }
		    out.println();
		    out.close();
	}

}
