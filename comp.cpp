#include<bits/stdc++.h>
using namespace std;
class job
{
public:
int id;
int deadline;
};
void swap(job j1,job j2)
{
int a,b;
a=j1.id;
j1.id=j2.id;
j2.id=a;
b=j1.deadline;
j1.deadline=j2.deadline;
j2.deadline=b;
}
void sort(job j[])
{
for(int i=0;i<5;i++)
{
for(int k=0;k<5;k++)
{
if(j[k].id>j[k+1].id)
{
swap(j[k],j[k+1]);
}}
}}

main()
{
job j[5];
for(int i=0;i<5;i++)
{
cout<<"Job"<<i+1;
cin>>j[i].id;
cin>>j[i].deadline;
}
sort(j);
for(int i=0;i<5;i++)
{
cout<<j[i].id<<endl;
}
return 0;
}
