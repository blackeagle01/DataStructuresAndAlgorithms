#include<bits/stdc++.h>
using namespace std;
class node
{
public:
int key;
node *lchild;
node *rchild;
};
node *root=NULL;
void bst(int x)
{
node *n=new node;
n->key=x;
if(root==NULL)
{
root=n;
n->lchild=NULL;
n->rchild=NULL;
}
else
{
node *temp=root;
while(true)
{
if(x<temp->key)
{
if(temp->lchild==NULL)
{
temp->lchild=n;
n->lchild=NULL;
n->rchild=NULL;
break;
}
temp=temp->lchild;
}
else
{
if(temp->rchild==NULL)
{
temp->rchild=n;
n->lchild=NULL;
n->rchild=NULL;
break;
}
temp=temp->rchild;
}
}
}
}
void sort(node *root)
{
if(root->lchild!=NULL)
{
sort(root->lchild);
}
cout<<root->key<<endl;
if(root->rchild!=NULL)
{
sort(root->rchild);
}
}
int extractmax(node *root)
{
node *temp=root;
if(root->rchild==NULL)
{
int x=root->key;
root=root->lchild;
root->rchild=NULL;
delete temp;
return x;
}
else
{
node *temp1=root->rchild;
while(temp1->rchild!=NULL)
{
temp=temp->rchild;
temp1=temp1->rchild;
}
int x=temp1->key;
delete temp1;
temp->rchild=NULL;
return x;
}
}
void search(node *root,int x)
{
if(x==root->key)
{
cout<<"Found";
return;
}
if(x>root->key)
{
if(root->rchild==NULL)
{
cout<<"Not found";
return;
}
else
{
search(root->rchild,x);
}
}
else
{
if(root->lchild==NULL)
{
cout<<"Not found";
return;
}
else
{
search(root->lchild,x);
}
}}
main()
{
int key[100];
cout<<"No of entries in tree";
int n;
cin>>n;
for(int i=1;i<=n;i++)
{
cin>>key[i];
}
for(int i=1;i<=n;i++)
{
bst(key[i]);
}
cout<<extractmax(root);
sort(root);
int x;
cout<<"search for";
cin>>x;
search(root,x);
return 0;
}
