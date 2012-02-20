import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;




public class FourSum {

	static public class ValWrapper{
		ArrayList<Integer> ali = null;
		public ValWrapper(ArrayList<Integer> v){
			ali = v;
		}
		public boolean equals(Object o)   
	    {   
	        if (this == o)   
	        {   
	            return true;   
	        }   
	        ValWrapper vw = (ValWrapper) o;
	        if(ali.get(0).equals(vw.ali.get(0)) && ali.get(1).equals(vw.ali.get(1)) 
	        		&&  ali.get(2).equals(vw.ali.get(2)))
	        	return true;
	        
	        return false;
	}
		//i hope it is right
		public int hashCode() {
				return ali.get(0).intValue() *51 + ali.get(1).intValue() * 131+ 
						ali.get(2).intValue() * 17 + ali.get(3).intValue();
		}
	}
	private HashSet<ValWrapper> lookTable = new HashSet<ValWrapper>();
	
	 public ArrayList<ArrayList<Integer>> fourSum(int[] num, int target) {
	        // Start typing your Java solution below
	        // DO NOT write main() function
		 lookTable.clear();
		 ArrayList<ArrayList<Integer>> aali = new ArrayList<ArrayList<Integer>>();
	        if(num.length < 4)
	        	return aali;
	        Arrays.sort(num);
	        
	        
	        for(int i = 0; i < num.length -3; i++){
	        	for(int j = i+1; j < num.length - 2; j++){
	        		for(int k = j+1; k < num.length - 1; k++){
	        			for(int f = k+1; f < num.length; f++){
	        				int sum = num[i] + num[j] + num[k] + num[f];
	        				if(sum == target){
	        					ArrayList<Integer> ali = new ArrayList<Integer>();
	        					ali.add(new Integer(num[i]));
	        					ali.add(new Integer(num[j]));
	        					ali.add(new Integer(num[k]));
	        					ali.add(new Integer(num[f]));
	        					if(!lookTable.contains(new ValWrapper(ali))){
	        						lookTable.add(new ValWrapper(ali));
	        						aali.add(ali);
	        					}
	        				}
	        				if(sum > target)
	        					break;
	        			}
	        			int tsum = num[i] + num[j] + num[k]*2;
	        			if(tsum > target)
	        				break;
	        		}
	        		int ssum = num[i] + num[j]*3;
	        		if(ssum > target)
	        			break;
	        	}
	        }
	        return aali;
	    }
	 
	    public void printf(ArrayList<ArrayList<Integer>> aali){
	    	for(ArrayList<Integer> ali : aali){
	    		for(Integer inte : ali){
	    			System.out.print(inte + "\t");
	    		}
	    		System.out.println();
	    	}
	    }
	    
	    
	    public static void main(String[] args){
	    	int[] num = {-3,-2,-1,0,0,1,2,3};
	    	FourSum fs = new FourSum();
	    	fs.printf(fs.fourSum(num, 0));
	    }
	 }
