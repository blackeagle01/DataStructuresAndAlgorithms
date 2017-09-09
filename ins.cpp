#include<bits/stdc++.h>
using namespace std;
void print(int a[],int n)
{
for(int i=0;i<n;i++)
{
cout<<a[i]<<endl;
}
}
main()
{
int a[]={3,2,4,6,5,7,9};
int n=sizeof(a)/sizeof(a[0]);
for(int j=1;j<n;j++)
{
for(int i=0;i<j;i++)
{
if(a[j]<a[i])
{
int t;
t=a[j];
a[j]=a[i];
a[i]=t;
}
}}
print(a,n);
return 0;
}
