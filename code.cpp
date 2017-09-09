#include<bits/stdc++.h>
using namespace std;
void swap(char *x,char *y)
{
char t;
t=*x;
*x=*y;
*y=t;
}
void reverse(string s,int i,int j)
{
if(i<j)
{
swap(&s[i],&s[j]);
reverse(s,i+1,j-1);
}
}
main()
{
string s;
cin>>s;
reverse(s,0,s.length()-1);
cout<<s;
return 0;
}
