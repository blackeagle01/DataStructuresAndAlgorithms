#include<bits/stdc++.h>
using namespace std;
void dfsvisit(int source,int adj[][20],int parent[],int n,int scp)
{
for(int i=1;i<=n;i++)
{
if(adj[source][i]==1)
{
parent[i]=source;
if(parent[scp]!=-1)
return;
dfsvisit(i,adj,parent,n,scp);
}
}}
int main()
{
int n;
cin>>n;
int adj[20][20];
for(int i=1;i<20;i++)
{
for(int j=1;j<20;j++)
{
adj[i][j]=0;
}}
while(true)
{
int a,b;
cout<<"Enter edge from "; cin>>a; if(a==99) break;cout<<"to"; cin>>b;
adj[a][b]=1;
}
int parent[20];
for(int i=1;i<=n;i++)
{
parent[i]=-1;
dfsvisit(i,adj,parent,n,i);
if(parent[i]!=-1)
{
cout<<"Cycle"<<endl;
return 0;
}
}
cout<<"NO CYCLE"<<endl;
return 0;
}
