#include<bits/stdc++.h>
using namespace std;
main()
{
int n;
cout<<"enter the no of nodes";
cin>>n;
int adj[20][20];
for(int i=1;i<=n;i++)
{
for(int j=1;j<=n;j++)
{
if(i==j)
adj[i][j]=0;
else
adj[i][j]=10000;
}
}
while(true)
{
int a,b,wt;
cout<<"enter edge from "; cin>>a; if(a==99) break; cout<<"to"; cin>>b;
cout<<"enter wt";
cin>>wt;
adj[a][b]=wt;
}
for(int k=1;k<=n;k++)
{
for(int i=1;i<=n;i++)
{
for(int j=1;j<=n;j++)
{
if(adj[i][j]==10000 and(adj[i][k]==10000 or adj[k][j]==10000 ))
continue;
if(adj[i][j]>adj[i][k]+adj[k][j])
adj[i][j]=adj[i][k]+adj[k][j];
}}}
for(int i=1;i<=n;i++)
{
for(int j=1;j<=n;j++)
{
cout<<adj[i][j]<<"\t";
}
cout<<endl;
}
return 0;
}
