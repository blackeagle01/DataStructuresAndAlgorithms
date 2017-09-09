#include<bits/stdc++.h>
using namespace std;
void dfsvisit(int adj[][20],vector<int> &parent,int source,int n)
{
for(int i=1;i<=n;i++)
{
if(parent[i]==-1)
{
if(adj[source][i]==1)
{
parent[i]=source;
dfsvisit(adj,parent,i,n);
}}}}
main()
{
int n;
cin>>n;
int adj[20][20];
while(true)
{
int a,b;
cout<<"Enter edge from "; cin>>a; if(a==99) break;cout<<"to"; cin>>b;
adj[a][b]=1;
}
int source,target;
vector<int> parent(n+1,-1);
cout<<"Enter source";
cin>>source;
cout<<"Enter target";
cin>>target;
dfsvisit(adj,parent,source,n);
if(parent[target]==-1)
cout<<"No path";
else
cout<<"Path";
return 0;
}
