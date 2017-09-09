#include<bits/stdc++.h>
using namespace std;
#define inf 100000;
bool allnotdone(vector<int> done[],int n)
{
for(int i=1;i<=n;i++)
{
if(done[i]!=1)
return true;
}
return false;
}
int extractmin(vector<int> ds[],int n)
{
int k=0,min=inf;
for(int i=1;i<=n;i++)
{
if(min>ds[i])
{
min=ds[i];
k=i;
}
}
return k;
}
void relaxall(int ds[],int node,int adj[][10],int n)
{
for(int i=1;i<=n;i++)
{
if(ds[i]>ds[node]+adj[node][i])
{
ds[i]=ds[node]+adj[node][i];
}
}}
main()
{
int adj[10][10];
int n;
cout<<"Number of nodes in graph";
cin>>n;
vector<int> ds(n+1,inf);
int source;
cout<<"Source?"; cin>>source;
ds[source]=0;
for(int i=1;i<n;i++)
{
for(int j=1;j<n;j++)
{
adj[i][j]=0;
}}
while(true)
{
int a,b;
cout<<"Edge from ": cin>>a; if(a==99) break; cout<<"TO"; cin>>b;
cout<<"Wt"; int wt; cin>>wt;
adj[a][b]=wt;
}
vector<int> done(n,0);
while(allnotdone(done,n))
{
int u=extractmin(ds,n);
relaxall(ds,u,adj,n);
done[u]=1;
}
for(int i=1;i<=n;i++)
{
cout<<ds[i]<<endl;
}
return 0;
}
