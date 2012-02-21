/*
ID: mryuan01
LANG: C++
TASK:gift1
*/

#include<stdio.h>
#include<map>
#include<vector>
#include<string>
#include<iostream>
#include<fstream>
using namespace std;
map<string, int> result;
vector<string> names;

int main()
{
	int n;
	string name;
	ifstream fin("gift1.in");
	ofstream fout("gift1.out");

	fin>>n;
	
	for(int i = 0; i < n; i++){
		fin>>name;
		names.push_back(name);
		result[name] = 0;
	}
	for(int i = 0; i < n; i++){
		int giver, nu;
		int out , in; 
		string gname;
		
		fin>>gname;
		fin>>giver>>nu;

		if(nu){
			out = giver / nu;
			in = giver % nu;
			result[gname] += in - giver;
		}

		for(int j = 0; j < nu; j++){
			string tmp;
			fin>>tmp;
			result[tmp] += out;
		}
	}

	for(int i = 0; i < n; i++){
		fout<<names[i]<<" " <<
			result[names[i]]<<endl;
		
	}
	
	return 0;
}
