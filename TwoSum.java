import java.util.Arrays;


public class TwoSum {
	static public class  Vwrapper implements Comparable<Vwrapper>{
		int val;
		int index;
		@Override
		public int compareTo(Vwrapper arg0) {
			// TODO Auto-generated method stub
			return this.val - arg0.val;
		}
		public Vwrapper(int val, int index){
			this.val = val;
			this.index = index;
		}
	}
	
    public int[] twoSum(int[] numbers, int target) {
        // Start typing your Java solution below
        // DO NOT write main() function
    	Vwrapper[] vw = new Vwrapper[numbers.length]; 
    	for(int i = 0; i < numbers.length; i++){
    		vw[i] = new Vwrapper(numbers[i], i);
    	}
    	Arrays.sort(vw);
        
    	int start = 0, end = numbers.length - 1;
    	while(end > start){
    		int sum = vw[end].val + vw[start].val;
    		if(sum == target){
    			int[] ret = new int [2];
    			if(vw[end].index > vw[start].index){
    				ret[0] = vw[start].index;
    				ret[1] = vw[end].index;
    			}else{
    				ret[0] = vw[end].index;
    				ret[1] = vw[start].index;
    			}
    			ret[0]++;
    			ret[1]++;
    			return ret;
    		}else if(sum > target){
    			end--;
    		}else{
    			start++;
    		}
    	}
    	return null;
    }
    
    public static void main(String[] args){
    	int[] A = {2, 7, 11, 15};
    	TwoSum ts = new TwoSum();
    	int [] ret = ts.twoSum(A, 9);
    	if(ret == null)
    		System.out.println("null");
    	else
    		System.out.println(ret[0] + "\t" + ret[1]);
    }
}
