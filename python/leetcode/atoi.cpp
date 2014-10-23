#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
class Solution {
public:
    int atoi(const char *str) {
        bool positive = true;
    	while(*str == ' ' || *str == '\t')
    		str++;
    	//determine signal
    	if(*str == '-'){
    		positive = false;
    		str++;
    	} else if(*str == '+') {
    		positive = true;
    		str++;
    	}
    
    	if(isdigit(*str) == false)
    		return 0;
    	int val = 0;
    	bool out = false;
    	while(isdigit(*str)) {
		  int cur = *str - '0', save = val;
		  val = val * 10 + cur;
		  if(val/10 != save)
    		{
    		    out = true;
    		    break;
    		}
    		str++;
    	}
		printf("%d %d\n", val, out);
    	if(positive == false)
    		val = -val;
    	if (out && positive)
    	    val = 2147483647;
    	if (out && !positive)
    	    val = -2147483648;
    	return val;
      
    }
};

int main()
{
  const char * p = "10522545459";
  Solution sol;
  printf("%d %d", sol.atoi(p), sol.atoi("2147483648"));
  return 0;
}
