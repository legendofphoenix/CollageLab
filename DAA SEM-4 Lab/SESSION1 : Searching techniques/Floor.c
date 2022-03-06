#include <stdio.h>
int main()
{
int t;
scanf("%d",&t);
while(t--)
{
int n,x,a[10],i;
scanf("%d%d",&n,&x);
for(i=0; i<n; i++)
scanf("%d",&a[i]);
for(i=n-1; i>=0; i--)
if (a[i] <= x)
break;
printf("%d\n",i);
}
return 0;
}
