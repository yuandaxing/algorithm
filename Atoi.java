
public class Atoi {
	public int errno = 0;
    public int atoi(String str) {
        // Start typing your Java solution below
        // DO NOT write main() function
    	str = str.trim();
    	int num = 0;
    	boolean positive = true;
    	int pos = 0;
    	if(str.length() == 0){
    		errno = 1;
    		return num;
    	}
    	if(str.charAt(0) == '-'){
    		positive = false;
    		pos++;
    	} else if(str.charAt(0) == '+'){
    		positive = true;
    		pos++;
    	}
    	boolean findOnedigit = false;
    	for(; pos < str.length(); pos++){
    		if(Character.isDigit(str.charAt(pos))){
    			findOnedigit = true;
    			int saved = num;
    			num = num * 10 + str.charAt(pos) - '0';
    			/*if(num < saved){
    				errno = 1;
    				if(positive)
    					return  Integer.MAX_VALUE;
    				else
    					return Integer.MIN_VALUE;
    			}*/
    		}else{
    			break;
    		}
    	}
    	if(!findOnedigit){
    		errno = 1;
    		return num;
    	}
    	
    	if(!positive && num > 0){
    		if(num == Integer.MAX_VALUE)
    			return Integer.MIN_VALUE;
    		return 0 - num;
    	}
    	if(positive && num < 0){
    		if(num == Integer.MIN_VALUE)
    			return Integer.MAX_VALUE;
    		return 0 - num;
    	}
    	return num;
    }
    
    public static void main(String[] args){
    	Atoi atoi = new Atoi();
    	System.out.println(atoi.atoi("-10000"));
    }

}
