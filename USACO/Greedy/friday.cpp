/*
ID: mryuan01
LANG: C++
TASK:friday
*/
#include <fstream>
#include <vector>
#include <iostream>

int LEAPYEAR(int n){
	if(n % 100 != 0 && n % 4 == 0)
		return 1;
	if(n % 400 == 0)
		return 1;
	return 0;
}   



int totalDayYear(int n)
{
	if(LEAPYEAR(n))
		return 366;
	return 365;
}
int dayofMonth(int year, int month)
{
	switch(month)
	{
		case 1:
		case 3:
		case 5:
		case 7:
		case 8:
		case 10:
		case 12:
			return 31;
		case 4:
		case 6:
		case 9:
		case 11:
			return 30;
		case 2:
			if(LEAPYEAR(year))
				return 29;
			else
				return 28;
	}
	
	//other case
	return 0;
}
using namespace std;
int main()
{
	int k[7] = {0};
	ifstream fin("friday.in");
	ofstream fout("friday.out");
	int nyear;
	int nday = 0;

	fin>>nyear;

	for(int i = 0; i < nyear; i++){
		for(int j = 0; j < 12; j++){
			nday += dayofMonth(1900 + i, j);
			k[(nday + 13) % 7]++;	
		}
		nday += dayofMonth(1900 + i, 12);
	}
	
	fout<<k[6];	
	for(int i = 0; i < 6 ; i++)
		fout<<" "<<k[i];
	fout<<endl;

	return 0;
}
