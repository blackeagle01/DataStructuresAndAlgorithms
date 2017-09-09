#include<bits/stdc++.h>
using namespace std;
main()
{
string s="My name is Harsh and my hobby is playing";
int x=0,count=0;
while(true)
{
x=s.find("is");
if(x==-1) break;
s.replace(x,2,"am");
count++;
}
cout<<s;
return 0;
}
