/*
ID: mryuan01
LANG: C++
TASK:beads
*/
#include <iostream>
#include <fstream>
#include <string.h>

using namespace std;
int leftGo(char *a, int len, int pos, int &At)
{
	int cur = pos, init = 0;
	int nc = 0;
	char ch;


	cur = (--cur + len) % len;
	while(pos != cur){
		if(a[cur] == 'w'){
			nc++;
		}else if(init == 0){
			init = 1;
			ch = a[cur];
			nc++;
		}else if(a[cur] == ch){
			nc++;
		}else
			break;			
		cur = (--cur + len) % len;
	}
	return nc;
}
int righGo(char *a, int len, int pos, int &At)
{
	int cur = pos, init = 0;
	int nc = 0;
	char ch;

	cur = (cur + len) % len;
	while((pos  - 1 + len) % len != cur){
		if(a[cur] == 'w'){
			nc++;
		}else if(init == 0){
			init = 1;
			ch = a[cur];
			nc++;
		}else if(a[cur] == ch){
			nc++;
		}
		else
			break;			
		cur = (++cur + len) % len;
	}
	return nc;
}
int main()
{
	int n;
	char a[1000];
	int max = 0;
	ifstream fin("beads.in");
	ofstream fout("beads.out");

	memset(a, 0, sizeof(a));
	
	fin>>n>>a;

	for(int i = 0; i <= n; i++){
		int nr, nl, rAt, lAt;
		nl = leftGo(a, n, i, lAt);
		nr = righGo(a, n, i, rAt);
		if(nl + nr >=  n){
			max = n;
			break;
		}
		if(max < nl + nr){
			max = nl + nr;
		}	
	}
	
	fout<<max<<endl;
	return 0;
}

