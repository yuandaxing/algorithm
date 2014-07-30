package org.java.cgcl;


public class LCSS {
	
	public static int[][] comput_LCSS(String stra, String strb){
		int[][]   matrix = new int[stra.length()][];
		for(int i = 0; i < stra.length(); i++){
			matrix[i] = new int[strb.length()];
		}
		for(int i = 0; i < stra.length(); i++){
			for(int j = 0; j < strb.length(); j++){
				if(stra.charAt(i) == strb.charAt(j)){
					if(i == 0 || j == 0){
						matrix[i][j] = 1;
					}else{
						matrix[i][j] = matrix[i - 1][j - 1] + 1;
					}
				}else{
					matrix[i][j] = 0;
				}
			}
		}
		
		return matrix;
	}
	
	
	public static String reverse(String str){
		StringBuffer sb = new StringBuffer();
		for(int i = str.length() - 1; i >= 0; i--){
			sb.append(str.charAt(i));
		}
		return sb.toString();
	}
	
public static void main(String[] args){
	String stra = "FourscoreandsevenyearsagoourfaathersbroughtforthonthiscontainentanewnationconceivedinzLibertyanddedicatedtothepropositionthatallmenarecreatedequalNowweareengagedinagreahtcivilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth";
	int[][] ret = comput_LCSS(stra, reverse(stra));
	int max = 0;
	int end = -1;
	for(int i = 0; i < ret.length; i++){
		for(int j = 0; j < ret[i].length; j++){
			if(ret[i][j] > max){
				max = ret[i][j];
				end = i;
			}
		}
	}
	
	for(int i = end - max +1; i <= end; i++){
		System.out.print(stra.charAt(i));
		
	}
}

}
