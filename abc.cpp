#include<bits/stdc++.h>
using namespace std;
void bsearch(int a[],int p,int q,int node)
{
if(p<=q)
{
int x=floor((p+q)/2);
if(a[x]==node)
{
cout<<"Found";
exit(1);
}
else if(a[x]<node)
{
bsearch(a,x+1,q,node);
}
else if(a[x]>node)
{
bsearch(a,p,x-1,node);
}
}
else
{
cout<<"Not found";
}
}
main()
{
int a[]={1,2,3,4,5,6,7,8,9};
int x;
cin>>x;
int n=sizeof(a)/sizeof(a[0]);
bsearch(a,0,n-1,x);
return 0;
}
