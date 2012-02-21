#include <stdio.h>

int ans[10];

void output()
{
for(int i=0;i<10;++i)
printf("%d ",ans[i]);
printf("\n");
}

bool test()
{
int num[10] = {};
for(int i=0;i<10;++i)
num[ans[i]] ++;
for(int i=0;i<10;++i)
if(ans[i] != num[i])
return 0;
return 1;
}

void solve(int po)
{
if(po == 9)
{
if(test())
output();
return ;
}
for(int i=0;i<10;++i)
{
ans[po] = i;
solve(po+1);
}
}

int main()
{
solve(0);
return 0;
}
