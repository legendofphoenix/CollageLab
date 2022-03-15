#include <stdio.h>
int main()
{
int n, a[10], i, max=0, min=100;
scanf("%d",&n);
for(i=0; i<n; i++)
scanf("%d",&a[i]);
for(i=0; i<n; i++)
{
if(min > a[i])
min = a[i];
if(max < a[i])
max = a[i]; }
printf("Minimum element in an array : %d\n",min);
printf("Maximum element in an array : %d",max);
return 0;
}
