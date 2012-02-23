import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
//import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

/*
ID: mryuan01
LANG: JAVA
TASK: packrec
*/
public class packrec {
	public static class Rectangle implements Comparable<Rectangle>{
		int h;
		int w;
		@Override
		public int compareTo(Rectangle arg0) {
			// TODO Auto-generated method stub
			return w - arg0.w;
		}
		
		public Rectangle makeStandard(){
			if(w > h){
				int tmp = w;
				w = h;
				h = tmp;
			}
			return this;
		}
		
		@Override
		public int hashCode() {
			final int prime = 31;
			int result = 1;
			result = prime * w + h;
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
			Rectangle other = (Rectangle) obj;
			return h == other.h && w == other.w;
		}

		public void rotate(){
			int tmp = w;
			w = h;
			h = tmp;
		}
		public Rectangle(int h, int w){
			this.h = h;
			this.w = w;
		}
		public Rectangle(){};
		
	}
	
	private static Rectangle[] rects = new Rectangle[4]; 
	private static int minArea = Integer.MAX_VALUE;
	private static ArrayList<Rectangle> ar = new ArrayList<Rectangle>();
	
	public static void swap(int i, int j){
		assert(i >= 0 && i < 4);
		assert(j >= 0 && j < 4);
		Rectangle tmp = rects[i];
		rects[i] = rects[j];
		rects[j] = tmp;
	}
	
	public static  int max(int ... arg){
		int max = 0;
		for(int a: arg){
			if(a > max)
				max = a;
		}
		return max;
	}
	public static void mayAdd(int h, int w){
		int area = h * w;
		if(area > minArea)
			return ;
		Rectangle r =new Rectangle(h, w).makeStandard();
		if(area == minArea ){
			if(!ar.contains(r))
				ar.add(r);
			
			
			return ;
		}
		
		ar.clear();
		minArea = area;
		ar.add(r);
	}
	public static void calculate6Case(){
		Rectangle r = new Rectangle();
		int h, w;
		//case one
		{
			 h = max(rects[0].h,rects[1].h,rects[2].h,rects[3].h);
			w = rects[0].w+rects[1].w+rects[2].w+rects[3].w;
			mayAdd(h, w);
		}
		//case two
		{
			h = rects[0].w + max(rects[1].h,rects[2].h,rects[3].h);
			w = max(rects[0]. h, rects[1].w+rects[2].w+rects[3].w);
			mayAdd(h, w);
		}
		//case three
		{
			h = max(rects[0].w + rects[1].h, rects[0].w + rects[2].h, rects[3].h);
			w = max(rects[3].w + rects[0].h,  rects[1].w+rects[2].w+rects[3].w);
			mayAdd(h, w);
		}
		
		//case four five
		{
			h = max(rects[0].h,rects[1].h +rects[2].h,rects[3].h);
			w = max(rects[0].w+rects[2].w+rects[3].w, rects[0].w+rects[1].w+rects[3].w);
			mayAdd(h, w);
		}
		
		//case six
		{
			if(rects[0].w <= rects[3].h){
				h = max(rects[0].w+rects[1].h,rects[2].w+rects[3].h);
				if(rects[3].h >=rects[0].w+rects[1].h ){
					w = max(max(rects[1].w, rects[0].h)  + rects[3].w, rects[2].h);
				}else if(rects[3].w >= rects[2].h){
					w = max(rects[1].w, rects[0].h)  + rects[3].w;
				}else	{
					w = max(rects[1].w + rects[2].h, rects[0].h + rects[3].w);
				}
				mayAdd(h, w);
			}
		}
	}
	
	public static void solve(int n){
		if(n == 4){
			calculate6Case();
			return ;
		}
		solve(n+1);
		rects[n].rotate();
		solve(n+1);
		rects[n].rotate();
	}
	
	public static void permutation(int start){
		if(start >= 4){
			//solve(0);
			solve(0);
		}
		for(int i = start; i < rects.length; i++){
			swap(start, i);
			permutation(start+1);
			swap(start, i);
		}
	}
	
	
	public static void main(String[]args) throws IOException{
		BufferedReader f = new BufferedReader(new FileReader("packrec.in"));
        // input file name goes above
		PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("packrec.out")));

		for(int i = 0; i < 4; i++){
			StringTokenizer st = new StringTokenizer(f.readLine());
			int w = Integer.parseInt(st.nextToken());
			int h = Integer.parseInt(st.nextToken());
			rects[i] = new Rectangle(h, w);
		}
		permutation(0);
		
//		for(Rectangle r : ar){
//			r.makeStandard();
//		}
		Collections.sort(ar);
		
		out.println(minArea);
		for(Rectangle r : ar){
			out.println(r.w+" "+r.h);
		}
		out.close();
		
	}
}
