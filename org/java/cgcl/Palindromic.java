package org.java.cgcl;

public class Palindromic {
	public static boolean checkPalindromicStr(String str){
			for(int i = 0, j = str.length() - 1; j > i; j--, i++ ){
				if(str.charAt(i) != str.charAt(j))
					return false;
			}
			return true;
	}
	public static String bruteLP(String s){
		String str = s;
		String ret = null;
		int start = 0;
		int max = 1;
		for(int i = 0; i < str.length(); i++){
			for(int j = i + 1; j < str.length(); j++){
				if(j - i +1 > max && checkPalindromicStr(str.substring(i, j+1))){
					start = i;
					max = j- i + 1;
				}
			}
		}
		
		return str.substring(start, start+max);
	}
	
	public static void printArray(int[][] arr){
		for(int i = 0; i < arr.length; i++){
			for(int j = 0; j < arr[i].length; j++){
				System.out.print(arr[i][j]+"\t");
			}
			System.out.println();
		}
	}
	public static String DP(String s){
		String str = s;
		int[][] matrix = new int [str.length()][];
		for(int i = 0; i < str.length(); i++){
			matrix[i] = new int[str.length()];
		}
		for(int i = 0; i < str.length(); i++){
			for(int j = 0; j < str.length(); j++){
				matrix[i][j] = 0;
			}
		}
		
		for(int len= 1; len <= str.length(); len++){
			for(int j = 0; j < str.length() - len + 1; j++){
				if(len == 1){
					matrix[j][j + len -1] = 1;
				}else if(str.charAt(j) == str.charAt(j + len -1)  &&(len == 2 || matrix[j+1][j + len - 2] != 0)){
					matrix[j][j + len -1] = matrix[j+1][j + len - 2] + 2;
				}
			}
		}
		
		
	//	printArray(matrix);
		int start = 0, end = 0, max = 0;
		for(int i = 0; i < str.length(); i++){
			for(int j = i; j < str.length(); j++){
				if(matrix[i][j] > max){
					max = matrix[i][j];
					start = i;
					end = j;
				}
			}
		}
		//System.out.println(max );
		return str.substring(start, end+1);
	}
	
	public static void main(String[] args){
		String str = "FourscoreandsevenyearsagoourfaathersbroughtforthonthiscontainentanewnationconceivedinzLibertyanddedicatedtothepropositionthatallmenarecreatedequalNowweareengagedinagreahtcivilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth";
		//System.out.print(bruteLP(str));
		String str1  = "bb";
		System.out.println(DP(str1));
		
		
		
		//System.out.println(bruteLP(str1));
	}

}
