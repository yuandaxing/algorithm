
public class RemoveDuplicate {
    public int removeDuplicates(int[] A) {
        // Start typing your Java solution below
        // DO NOT write main() function
    	int len = A.length;
    	int j;
        for(int i = 0; i < len; i++){
        	j = i + 1;
        	while(j < len && A[j] == A[i]) j++;
        	if(j - i > 1){ // then we should move the same element
        		int move = j - i - 1;
        		for(int k = j; k < len; k++)
        			A[k - move] = A[k];
        		len -= move ;
        	}
        }
        return len;
    }
    
    
    public int removeElement(int[] A, int elem) {
        // Start typing your Java solution below
        // DO NOT write main() function
    	int len = 0;
        for(int i = 0; i < A.length; i++){
        	if(A[i] != elem)
        		A[len++] = A[i];
        }
        return len;
    }
    public static void main(String[] args){
    	RemoveDuplicate rd = new RemoveDuplicate();
    	int[] A = {1,1,2};
    	System.out.println(rd.removeDuplicates(A));
    }
}
