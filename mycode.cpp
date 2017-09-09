#include<bits/stdc++.h>
using namespace std;
main()
{
int a[]={1,2,2,1,9,3,4,5,4,3,6,7,8,7,7,7,5,6,7,4,5,3,2,3,5,6,7};
int buffer[10];
vector<int> hash(10,0);
int n=sizeof(a)/sizeof(a[0]);
int k=0;
for(int i=0;i<n;i++)
{
if(hash[a[i]]==0)
{
hash[a[i]]=1;
buffer[k]=a[i];
k++;
}
}
for(int i=0;i<k;i++)
{
cout<<buffer[i]<<"\t";
}
return 0;
}
