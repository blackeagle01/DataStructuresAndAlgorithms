#include<bits/stdc++.h>
using namespace std;
main()
{
int a[3][3][3][3];
for(int k=0;k<3;k++)
{
for(int l=0;l<3;l++)
{
for(int i=0;i<3;i++)
{
for(int j=0;j<3;j++)
{
a[k][l][i][j]=0;
}}}}
while(true)
{
cout<<"Enter grid coordinates";
int m,n;
cin>>m; if(m==99) break;
cin>>n;
cout<<"Enter position in grid";
int a,b;
cin>>a>>b;
cout<<"Enter number";
int x;
cin>>x;
a[m][n][a][b]=x;
}
for(int k=0;k<3;k++)
{
for(int l=0;l<3;l++)
{
for(int i=0;i<3;i++)
{
for(int j=0;j<3;j++)
{
cout<<a[k][l][i][j]<<"  ";
}
cout<<endl;
}
}
cout<<endl;
}
return 0;
}

