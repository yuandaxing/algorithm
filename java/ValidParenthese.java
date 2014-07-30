import java.util.Stack;


public class ValidParenthese {
	public  boolean validPair(char a, char b){
		if(a == '(' && b == ')')
			return true;
		if(a == '[' && b == ']')
			return true;
		if(a == '{' && b == '}')
			return true;
		return false;
	}
    public boolean isValid(String s) {
        // Start typing your Java solution below
        // DO NOT write main() function
        Stack<Character> sc = new  Stack<Character>();
        for(int i = 0; i < s.length(); i++){
        	char c = s.charAt(i);
        	
        	if(c == '(' || c == '[' || c == '{'){
        		sc.add(new Character(c));
        	}else{
        		if(sc.empty())
        			return false;
        		Character pop = sc.remove(sc.size() - 1);
        		if(!validPair(pop.charValue(), c))
        			return false;
        	}
        }
        if(sc.empty())
        	return true;
        else
        	return false;
    }
    
    public static void main(String[] args){
    	String par = "{[}[{}{{({)){[}([]{)}({())[}[}";
    	String par1 = "()({}[])[]{}";
    	ValidParenthese vp = new ValidParenthese();
    	assert(vp.isValid(par) == false);
    	assert(vp.isValid(par1));
    	
    }
    
    
    
}
