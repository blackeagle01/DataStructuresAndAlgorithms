#include<bits/stdc++.h>
using namespace std;
class node
{
public:
int x;
node *next;
};
node *first=NULL;
void insert(int val)
{
node *f=new node;
f->x=val;
if(first==NULL)
{
first=f;
f->next=NULL;
}
else
{
node *temp=first;
while(temp->next!=NULL)
{
temp=temp->next;
}
temp->next=f;
f->next=NULL;
}}
void showlist()
{
node *temp=new node;
temp=first;
while(temp!=NULL)
{
cout<<temp->x<<"\t";
temp=temp->next;
}
}
main()
{
int n;
int i=0;
while(i<4)
{
cin>>n;
insert(n);
i++;
}
showlist();
return 0;
}
