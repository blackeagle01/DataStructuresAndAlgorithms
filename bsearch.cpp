#include<bits/stdc++.h>
using namespace std;
void bsearch(int a[],int i,int j,int key)
{
if(i<=j)
{
int m=floor((i+j)/2);
if(a[m]==key)
{
cout<<"Found";
return;
}
else if(a[m]>key)
{
bsearch(a,i,m-1,key);
}
else if(a[m]<key)
{
bsearch(a,m+1,j,key);
}
}
}
main()
{
int a[]={1,2,3,4,5,6};
int x; cin>>x;
bsearch(a,0,5,x);
return 0;
}
