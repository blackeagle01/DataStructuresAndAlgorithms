#include<bits/stdc++.h>
using namespace std;
int arr[3][3];
void init()
{
for(int i=0;i<3;i++)
{
for(int j=0;j<3;j++)
{
arr[i][j]=0;
}}
}
bool safe(int k)
{
for(int i=0;i<3;i++)
{
for(int j=0;j<3;j++)
{
if(arr[i][j]==k)
{
return false;
}}}
return true;
}
void fill(int i,int j,int num)
{
arr[i][j]=num;
}
void solve()
{
for(int i=0;i<3;i++)
{
for(int j=0;j<3;j++)
{
if(arr[i][j]==0)
{
for(int k=1;k<10;k++)
{
if(safe(k))
{
arr[i][j]=k;
solve();
}
}
}
}
}
}
void print()
{
for(int i=0;i<3;i++)
{
for(int j=0;j<3;j++)
{
cout<<arr[i][j]<<" ";
}
cout<<endl;
}}
main()
{
init();
fill(0,0,1);
fill(2,2,5);
fill(1,2,4);
solve();
print();
return 0;
}
