#include <stdio.h>
int main()
{
int t;
scanf("%d",&t);
while(t--)
{
int n;
scanf("%d",&n);
if(n<5)
printf("%d\n",n*5);
else
printf("%d\n",--n*5);
}
return 0;
}
