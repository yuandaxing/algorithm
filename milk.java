import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;


/*
ID: mryuan01
LANG: JAVA
TASK: milk
*/
public class milk {
	
	public static class MilkContainer implements Comparable<MilkContainer>{
		int vol;
		int price;
		
		public MilkContainer(int vol, int price){
			this.vol = vol;
			this.price = price;
		}
		@Override
		public int compareTo(MilkContainer arg0) {
			// TODO Auto-generated method stub
			int ret = this.price - arg0.price;
			return  ret > 0 ? 1 : (ret < 0 ? -1 : 0);
		}
	}
	
	public static int getMinMoney(int total, MilkContainer[] milks){
		Arrays.sort(milks);
		int pos = 0;
		int money = 0;
		while(total > 0 && pos < milks.length){
			MilkContainer mc = milks[pos++];
			
			if(total > mc.vol){
				total -= mc.vol;
				money += mc.vol * mc.price;
			}else{
				money += mc.price * total;
				total = 0;
			}
		}
		return money;
	}
	
	public static void main(String[]args) throws IOException{
		BufferedReader f = new BufferedReader(new FileReader("milk.in"));
        // input file name goes above
		PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("milk.out")));
// Use StringTokenizer vs. readLine/split -- lots faster
		StringTokenizer st = new StringTokenizer(f.readLine().trim());
		int total = Integer.parseInt(st.nextToken());
		int num =  Integer.parseInt(st.nextToken());
		MilkContainer[] milks = new MilkContainer[num];
		for(int i = 0; i < num; i++ ){
			st =  new StringTokenizer(f.readLine().trim());
			int price = Integer.parseInt(st.nextToken());
			int vol = Integer.parseInt(st.nextToken());
			milks[i] = new MilkContainer(vol, price);
		}
		
		out.println(getMinMoney(total, milks));
		out.close();
	}
}
