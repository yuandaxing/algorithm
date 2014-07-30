import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.HashSet;

/*
ID: mryuan01
LANG: JAVA
TASK: namenum
*/
public class namenum {
	public static String[] map = {"", "", "ABC", "DEF","GHI", "JKL","MNO","PRS","TUV","WXY"};
	private static HashSet<String> hs = new HashSet<String>(); 
	public static boolean found = false;
	static{
		 try {
			BufferedReader f = new BufferedReader(new FileReader("dict.txt"));
			String key = null;
			while((key = f.readLine()) != null){
				hs.add(key.trim());
			}
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	public static void findName(String num, int start, StringBuffer sb, PrintWriter out){
		if(start == num.length()){
			String name = sb.toString();
			if(hs.contains(name)){
				out.println(name);
				found = true;
			}
			return ;
		}
		int len = sb.length();
		String  s1 = map[num.charAt(start) - '0'];
		for(int i = 0; i <  s1.length(); i++ ){
			sb.append(s1.charAt(i));
			findName(num, start+1, sb, out);
			sb.deleteCharAt(len);
		}
	}

	  public static void main (String [] args) throws IOException {
		    // Use BufferedReader rather than RandomAccessFile; it's much faster
		    BufferedReader f = new BufferedReader(new FileReader("namenum.in"));
		                                                  // input file name goes above
		    PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("namenum.out")));
		    // Use StringTokenizer vs. readLine/split -- lots faster
		    String s = f.readLine().trim();
		    StringBuffer sb = new StringBuffer();
		    findName(s, 0, sb, out);
		    if(!found){
		    	out.println("NONE");
		    }
		    out.close();
	  }
}
