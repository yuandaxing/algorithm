
public class ReverseInteger {

	 public int reverse(int x) {
	        // Start typing your Java solution below
	        // DO NOT write main() function
		 	int inte = x;
		 	boolean positive = (x >= 0) ;
			int reverse = 0;
			if(inte < 0)
				inte = 0 - inte;
			while(inte != 0){
					int tail =  inte % 10;
					reverse = reverse * 10 + tail;
					inte /= 10;
				}
			if(positive)
				return reverse;
			else
				return 0 - reverse;
	    }
}
