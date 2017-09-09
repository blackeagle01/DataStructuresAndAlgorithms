#include<bits/stdc++.h>
using namespace std;
int maxheight(int comp[][20],int h[],int done[],int k,int n)
{
if(alldone(done,n) or notcompatible(k,done,n))
return 0;
else
{
for(int i=1;i<=n;i++)
{
if(comp[k][i]==1)
{
done[i]=1;
a[u]=h[i]+maxheight(comp,h,n,i);
main()
{
int n;
cout<<"Enter number of boxes";
cin>>n;
int l[n+1],w[n+1],h[n+1];
for(int i=1;i<=n;i++)
{
cout<<"Length of box"<<i;
cin>>l[i];
cout<<"Width of box"<<i;
cin>>w[i];
cout<<"Height of box"<<i;
cin>>h[i];
}
int comp[n+1][20];
for(int i=1;i<=n;i++)
{
for(int j=1;j<=n;j++)
{
if(i==j)
comp[i][j]=0;
if(l[i]>l[j] and w[i]>w[j])
comp[i][j]=1;
else
comp[i][j]=0;
comp[0][j]=1;
}
cout<<maxheight(comp,h,n,0);
