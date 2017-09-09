#include<iostream>
using namespace std;
void swap(int *x,int *y)
{
int t;
t=*x;
*x=*y;
*y=t;
}
main()
{
int a[100];
int n;
cin>>n;
for(int i=0;i<n;i++)
{
cin>>a[i];
}
for(int i=0;i<n;i++)
{
int min=1000;
int k=i;
for(int j=i;j<n;j++)
{
if (a[j]<min)
{
min=a[j];
k=j;
}
}
swap(&a[i],&a[k]);
}
for(int i=0;i<n;i++)
{
cout<<a[i]<<" ";
}
cout<<endl;
return 0;
}
