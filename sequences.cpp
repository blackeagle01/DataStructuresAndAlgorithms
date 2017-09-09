#include<bits/stdc++.h>
using namespace std;
int sequences(int jumps[],int reachable[][30],int memo[],int n)
{
if(memo[n]!=-1)
return memo[n];
if(n==1)
{
memo[n]=0;
return memo[n];
}
else
{
int count=0;
for(int i=1;i<=n;i++)
{
if(reachable[i][n]==1)
{
count++;
}
}
memo[n]=count+sequences(jumps,reachable,memo,n-1);
return memo[n];
}
}
main()
{
int n;
cin>>n;
cout<<"Enter the matrix";
int a[n+1];
for(int i=1;i<=n;i++)
{
cin>>a[i];
}
int jumps[n+1];
for(int i=1;i<=n;i++)
{
jumps[i]=1;
if(a[i]<2)
jumps[i]=2;
if(a[i]==2 and a[i+1]<7)
jumps[i]=2;
}
int memo[n+1];
int reachable[n+1][30];
for(int i=1;i<=n;i++)
{
memo[i]=-1;
for(int j=1;j<=n;j++)
{
if(i>j or j>i+jumps[i])
reachable[i][j]=0;
else if(i==j)
reachable[i][j]=0;
else if(j<=i+jumps[i])
reachable[i][j]=1;
}
}
cout<<sequences(jumps,reachable,memo,n);
return 0;
}
