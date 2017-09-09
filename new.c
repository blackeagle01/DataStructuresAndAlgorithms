#include<stdio.h>
#include<math.h>
int func(int x,int y)
{
	return x+y;
}
int main()
{
	int x;
	printf("%s\n","enter the value of x" );
	scanf("%d",&x);
	printf("%d\n",pow(func(x,10),4) );
	return 0;

}