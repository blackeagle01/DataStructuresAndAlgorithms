#include<bits/stdc++.h>
using namespace std;
class student
{
public:
string name;
int roll;
};
class node
{
public:
int key;
student s;
node *lchild;
node *rchild;
};
node *root=NULL;
void bst(student &s,int x)
{
node *n=new node;
n->key=x;
(n->s).name=s.name;
(n->s).roll=s.roll;
node *temp=root;
if(root==NULL)
{
root=n;
n->lchild=NULL;
n->rchild=NULL;
}
else
{
while(true)
{
if(x>temp->key)
{
if(temp->rchild==NULL)
{
temp->rchild=n;
n->lchild=NULL;
n->rchild=NULL;
break;
}
else
{
temp=temp->rchild;
}
}
else
{
if(temp->lchild==NULL)
{
temp->lchild=n;
n->lchild=NULL;
n->rchild=NULL;
break;
}
else
{
temp=temp->lchild;
}
}}}}
void showdata(node *root)
{
if(root->lchild!=NULL)
{
showdata(root->lchild);
}
cout<<(root->s).name<<"    "<<(root->s).roll<<endl;
if(root->rchild!=NULL)
{
showdata(root->rchild);
}
}
int main()
{
student s[4];
for(int i=1;i<4;i++)
{
cout<<"Enter name";
cin>>s[i].name;
cout<<"Enter roll no";
cin>>s[i].roll;
bst(s[i],rand()%1000);
}
return 0;
}

