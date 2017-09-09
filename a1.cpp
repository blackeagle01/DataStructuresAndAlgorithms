#include<bits/stdc++.h>
using namespace std;
int ways(int dict[],int sum,int c[],int n)
{
if(dict[sum]!=-1)
{
return dict[sum];
}
if(sum==0)
return 1;
if(sum<0)
return 0;
int k=0;
for(int i=1;i<=n;i++)
{
k+=ways(dict,sum-c[i],c,n);
dict[sum]=k;
}
return dict[sum];
}
main()
{
int sum=0,n=0;
cin>>sum>>n;
int c[n+1];
c[0]=0;
for(int i=1;i<=n;i++)
{
cin>>c[i];
}
int dict[sum+1];
for(int i=0;i<=sum;i++)
{
dict[i]=-1;
}
cout<<ways(dict,sum,c,n);
return 0;
}
