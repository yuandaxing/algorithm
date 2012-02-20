
public class MedianOfTwoSortArray {
	
	int binary_K(int A[], int B[], int ni, int nj, int K)
	{
		int left = 0,  right = ni - 1;

		K--; //we need to find the K-- which is less than A[mid]
		while(right >= left){
			int mid = (left + right) / 2;

			if( K - mid < 0){
				right = mid - 1;
			}else if(K - mid > nj || (K - mid - 1) >= 0 && B[K - mid - 1] > A[mid]){
				left = mid + 1;
			}else if(K - mid < 0 || K - mid < nj && B[K - mid] < A[mid]){
				right = mid - 1;
			}else {
				return mid;
			}
		}
		return -1;
	}
	int find_K_2(int A[], int B[], int lenA, int lenB, int K)
	{
		assert(K > 0 && K <= lenA + lenB);

		int i;
		if((i = binary_K(A, B, lenA, lenB, K)) >= 0)
			return A[i];
		return B[binary_K(B, A, lenB, lenA, K)];
	}
    public double findMedianSortedArrays(int A[], int B[]) {
        // Start typing your Java solution below
        // DO NOT write main() function
    	int len = A.length + B.length;
    	if(len % 2 == 1){
    		return find_K_2(A, B, A.length, B.length, (len + 1) /2);
    	}
    	
    	int median1 = find_K_2(A, B, A.length, B.length, (len + 1) /2);
    	int median2 = find_K_2(A, B, A.length, B.length, (len + 2) /2);
    	return (median1 * 1.0 + median2) / 2;
    }
    
    
    
    
    public static void main(String[] args){
    	int[] A = {3,5};
    	int[] B = {1,2,4,6,7};
    	MedianOfTwoSortArray mosa = new MedianOfTwoSortArray();
    	
    	System.out.println(mosa.findMedianSortedArrays(A, B));
    }

}
