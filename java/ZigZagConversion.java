
public class ZigZagConversion {
	/*
	 * n row 
	 * first row
	 * k % (2n - 2) == 0 the first row
	 * last row
	 * k % (2n - 2) == n - 1;
	 * for mid i;
	 * k % (2n - 2) == i or 2n - 2 -  i
	 */
	StringBuffer getStringPeak(String text, int pos, int cycl){
		StringBuffer sb = new StringBuffer(); 
		for(int k = 0, cur = k * cycl + pos; cur < text.length(); k++, cur = k * cycl + pos){
			sb.append(text.charAt(cur));
		}
		return sb;
	}
	StringBuffer getStringMid(String text, int posl, int posr, int cycl){
		int cur = posl, k = 0;
		StringBuffer sb = new StringBuffer();
		boolean goRight = true;
		while(cur < text.length()){
			sb.append(text.charAt(cur));
			if(goRight)
				cur = k * cycl + posr;
			else{
				k++;
				cur = k * cycl + posl;
			}
			goRight = !goRight;
		}
		return sb;
	}
	String convert(String text, int nRows){
		int cycl = 2 * nRows - 2;
		StringBuffer sb = getStringPeak(text, 0, cycl);
		for(int i = 1; i < nRows - 1; i++ ){
			sb.append(getStringMid(text, i, cycl - i, cycl));
		}
		sb.append(getStringPeak(text, nRows - 1, cycl));
		
		
		return sb.toString();
	}
	
	public static void main(String[] args){
		ZigZagConversion zzc = new ZigZagConversion();
		String text = "PAYPALISHIRING";
		System.out.println(zzc.convert(text, 3));
	}
	

}
