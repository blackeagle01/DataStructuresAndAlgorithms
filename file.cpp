#include<bits/stdc++.h>
#include"prq.h"
using namespace std;
main()
{
priorityQ q;
q.insert(3);
q.insert(4);
cout<<q.extractmin();
cout<<q.extractmin();
return 0;
}
