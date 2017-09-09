#include<bits/stdc++.h>
using namespace std;
main()
{
string s[4];
s[1]="E->E+T";
s[0]="T->a";
s[2]="E->null";
for(int i=0;i<3;i++)
{
if(s[i][0]==s[i][3])
{
cout<<"Left recursive";
exit(1);
}
}
return 0;
}
