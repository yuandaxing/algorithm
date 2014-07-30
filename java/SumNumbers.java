import java.util.HashMap;
import java.util.Map;
import java.util.Vector;


public class SumNumbers {
	private int count = 0;
	
	Map<Integer, Integer> map = new HashMap<Integer, Integer>();
	Integer[] arrI = null;
	Vector<Integer> set = new Vector<Integer>();
	int sum = 0;
	
	void init(int[] array){
		arrI = new Integer[array.length];
		for(int i = 0; i < array.length; i++){
			arrI[i] = new Integer(array[i]);
			map.put(arrI[i], arrI[i] );
		}
	}
	boolean isExist(Integer i){
		return map.get(i) != null;
	}
	
	void comSum(int[] array, int start, int sum, int seti, boolean add){
		if(add && seti > 1 && isExist(new Integer(sum))){
			count++;
		}
		if(sum >= array[array.length -1] || start>= array.length)
			return ;
		comSum(array, start+1, sum + array[start], seti+1, true);
		comSum(array, start+1, sum, seti, false);
		}
	void comSet(int [] array, int start){
		if(start >= array.length){
			count++;
			return ;
		}
			sum += array[start];
			comSet(array, start+1);
			sum -= array[start];
			comSet(array, start+1);
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] array = {1, 2, 3, 4, 6};
		int [] array1={3,	4,9,14,	15,	19,	28,	37,	47,	50,	54,	56,	59,	61,	70,	73,	78,	81,	92,	95,	97,	99};
		SumNumbers sn = new SumNumbers();
		sn.init(array1);
		sn.comSum(array1, 0, 0, 0, false);
		System.out.print(sn.count);
	}
}
