#include<bits/stdc++.h>
using namespace std;
main()
{
int m1[3][3],m2[3][3],r[3][3];
for(int i=0;i<3;i++)
{
for(int j=0;j<3;j++)
{
cin>>m1[i][j];
m2[i][j]=m1[i][j];
}}
for(int i=0;i<3;i++)
{
for(int j=0;j<3;j++)
{
int sum=0;
for(int k=0;k<3;k++)
{
sum+=m1[i][k]*m2[k][j];
}
r[i][j]=sum;
}
}
for(int i=0;i<3;i++)
{
for(int j=0;j<3;j++)
{
cout<<r[i][j]<<"\t";
}
cout<<"\n";
}
return 0;
}
