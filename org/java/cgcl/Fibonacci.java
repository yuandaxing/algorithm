package org.java.cgcl;

import java.util.BitSet;
import java.util.Vector;

public class Fibonacci {
	public static class PrimeConainer{
		Vector<Integer> container = new Vector<Integer>();
		void add(int i){
			container.add(new Integer(i));
		}
		int getMax(){
			if(container.isEmpty())
				return -1;
			return container.lastElement().intValue();
			
		}
		public boolean maybePrime(int i){
				for(Integer iter : container){
					if(i % iter.intValue() == 0){
						return false;
					}
				}
				return true;
		}
		public int sumDiv(int k){
			int sum = 0;
			for(Integer iter : container){
				if(k % iter.intValue() == 0){
					sum += iter.intValue();
				}
			}
			return sum;
		}		
	}
		
		static public boolean isPrime(int inter, PrimeConainer c){
			int i = (int) (Math.sqrt(inter) + 1);
			int max = c.getMax();
			if(max == -1){
				BitSet bs = new BitSet(i+1);
				bs.clear();
				for(int j = 2; j <= i; j++){
					if(bs.get(j) == false){
						c.add(j);
						for(int k = 2, iter = j *k; iter <= i; k++, iter = k*j){
							bs.set(iter);
						}
					}else{
						continue;
					}
				}
			}else{
				if(c.maybePrime(inter) == false)
					return false;
				for(int j = max + 1; j <= i; j++){
					if(c.maybePrime(j)){
						c.add(j);
					}else{
						continue;
					}
				}
			}
			
			if(c.maybePrime(inter)){
				return true;
			}else{
				return false;
			}		 
	}
		
		public static void main(String[] args){
			PrimeConainer pc = new PrimeConainer();
			int k = 227000;
			int z = 415;
		
			int f1 = 0, f2 = 1, tmp;
			for(; f2 < k; tmp = f1, f1 = f2, f2 = f2 + tmp);
			
			System.out.println(f2);
			
			while(!isPrime(f2, pc)){
				tmp = f1;
				f1 = f2;
				f2 = f2 + tmp;
			}
			System.out.println(f2);
			System.out.println(pc.sumDiv(f2+1));
		}
}
