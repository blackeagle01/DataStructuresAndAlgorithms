#include<bits/stdc++.h>
using namespace std;
int arr[9][9];
void init()
{
for(int i=0;i<9;i++)
{
for(int j=0;j<9;j++)
{
arr[i][j]=0;
}}
}
void solve()
{
for(int i=0;i<9;i++)
{
for(int j=0;j<9;j++)
{
if(arr[i][j]==0)
{
for(int k=1;k<10;k++)
{
if(safe(i,j,k))
{
arr[i][j]=k;
solve();
}
else
{
arr[i][j]
}

main()
{
