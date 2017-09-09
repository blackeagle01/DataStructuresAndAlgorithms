#include<bits/stdc++.h>
using namespace std;
int max(int a,int b)
{
if(a>b)
return a;
else
return b;
}
int L(string str,int i,int j)
{
if(i>j)
return 0;
else if(i==j)
return 1;
else if(str[i]==str[j])
{ return 2+ L(str,i+1,j-1);
}
else
{
return max(L(str,i,j-1),L(str,i+1,j));
}
}
main()
{
string str;
cin>>str;
cout<<L(str,0,str.length()-1);
return 0;}

