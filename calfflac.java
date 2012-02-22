import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.StringTokenizer;

/*
ID: mryuan01
LANG: JAVA
TASK: calfflac
*/
public class calfflac {
public static 	boolean isSame(char a, char b){
		if(a != b)
			return Character.toLowerCase(a) == Character.toLowerCase(b);
		else
			return true;
	}
	public static String findLongestMid(String src,int left, int right){
		while(left >= 0 && right <= src.length() - 1){
			while(left >= 0 && !Character.isLetter(src.charAt(left))) 
				left--;
			while(right < src.length() && !Character.isLetter(src.charAt(right)))
					right++;
			if(left < 0 || right >= src.length()){
				if(left >= 0 )
					left++;
				if(right < src.length())
					right--;
				
					break;
			}
			if(!isSame(src.charAt(left), src.charAt(right))){
					left++;
					right--;
					break;
			}
			left--;
			right++;
		}
		left = left < 0 ? 0 : left;
		right = right >= src.length() ? src.length() - 1 : right;
		
		while(left < src.length() && !Character.isLetter(src.charAt(left))) 
			left++;
		while(right >= 0 && !Character.isLetter(src.charAt(right))) 
			right--;
		if(right >= left)
			return src.substring(left, right+1);
		return "";
		
	}
	public static int getpalindromeLen(String src){
		int len = 0;
		for(int i = 0; i < src.length(); i++){
			if(Character.isLetter(src.charAt(i)))
				len++;
		}
		return len;
	}
	public static String getLongest(String src){
		String maxString = "";
		int maxLen = 0, sublen1, sublen2, maxSublen;
		String sub1, sub2, maxsub;
		for(int i = 0; i < src.length() - 1; i++){
			if(Character.isLetter(src.charAt(i))){
				sub1 = findLongestMid(src, i, i);
				sublen1 = getpalindromeLen(sub1);
				sub2 = findLongestMid(src, i, i+1);
				sublen2 = getpalindromeLen(sub2);
				if(sublen1 > sublen2){
					maxsub = sub1;
					maxSublen = sublen1;
				}else{
					maxsub = sub2;
					maxSublen = sublen2;
				}

				if(maxSublen > maxLen){
					maxLen = maxSublen;
					maxString = maxsub;
				}
			}
		}
		return maxString;
	}
	
	public static void main(String[]args) throws IOException{
		BufferedReader f = new BufferedReader(new FileReader("calfflac.in"));
        // input file name goes above
		PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("calfflac.out")));
		StringBuffer sb = new StringBuffer();
		char[] buff = new char[128];
		int readlen = 0;
		while((readlen = f.read(buff)) != -1){
			sb.append(buff, 0, readlen);
		}
		String max = getLongest(sb.toString());
		int len = getpalindromeLen(max);
		out.println(len);
		out.println(max);
		out.close();
	}

}
