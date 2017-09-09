#include<bits/stdc++.h>
using namespace std;
bool safe(int current,int adj[][20],int c,vector<int> &color,int n)
{
for(int i=1;i<=n;i++)
{
if(adj[current][i]==1)
{
if(color[i]==c)
return false;
}
}
return true;
}
void graphcolor(int adj[][20],vector<int> &color,int current,int n)
{
for(int c=1;c<=n;c++)
{
if(safe(current,adj,c,color,n))
{
color[current]=c;
break;
}
}
for(int i=1;i<=n;i++)
{
if(color[i]==0)
graphcolor(adj,color,i,n);
}
}
int main()
{
cout<<"Enter the number of nodes";
int n;
cin>>n;
int adj[20][20];
for(int i=1;i<20;i++){
for(int j=1;j<20;j++)
{
adj[i][j]=0;
}}
while(true)
{
int a,b;
cout<<"Enter edge from "; cin>>a; if(a==99) break;cout<<"to"; cin>>b;
adj[a][b]=1;
adj[b][a]=1;
}
vector<int> color(n+1,0);
graphcolor(adj,color,1,n);
int mi=0;
for(int i=1;i<=n;i++)
{
if(color[i]>mi)
mi=color[i];
}
cout<<"Graph can be colored in minimum "<<mi<<" colors"<<endl;
for(int i=1;i<=n;i++)
{
cout<<"Node "<<i<<"="<<color[i]<<endl;
}
return 0;
}
