#include <stdio.h>
int main()
{
int t;
scanf("%d",&t);
while(t--)
{
int n, a[10], i, temp[100]={0};
scanf("%d",&n);
for(i=0; i<n; i++)
scanf("%d",&a[i]);
for(i=0; i<n; i++)
temp[a[i]] += 1;
for(i=0; i<100; i++)
if(temp[i] == 1)
printf("%d\n",i);
}
return 0;
}
