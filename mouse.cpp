#include<bits/stdc++.h>
using namespace std;
main()
{
int mouse[101][101],cat1[101][101],cat2[101][101];
int n,m,k;
cin>>m>>n;
cin>>k;
int xm[k],ym[k],xc1[k],yc1[k],xc2[k],yc2[k];
for(int i=0;i<k;i++)
{
cin>>xm[i]>>ym[i]>>xc1[i]>>yc1[i]>>xc2[i]>>yc2[i];
}
int a=0;
A :while(a<k)
{

for(int i=0;i<m;i++)
{
for(int j=0;j<n;j++)
{
if((i==1 or j==1) or (i==m or j==n))
{
mouse[i][j]=abs(xm[a]-i)+abs(ym[a]-j);
cat1[i][j]=abs(xc1[a]-i)+abs(yc1[a]-j);
cat2[i][j]=abs(xc2[a]-i)+abs(yc2[a]-j);
if(mouse[i][j]<cat1[i][j] and mouse[i][j]<cat2[i][j])
{
cout<<"YES"<<endl;
a++;
goto A;
}
}
}}
cout<<"NO"<<endl;
a++;
}
return 0;
}

