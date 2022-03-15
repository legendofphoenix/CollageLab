#include <stdio.h>
int main()
{
int t;
scanf("%d",&t);
while (t--)
{
int n , a[10] , i , j , sum = 0 , max = 0;
scanf("%d",&n);
for(i=0; i<n; i++)
{
scanf("%d",&a[i]);
if ( a[i] > max )
max = a[i];
}
for(i=0; i<n; i++)
for(j=i+1; j<n; j++)
sum += abs (a[i] - a[j]);
printf("%d\n",sum*max);
}
return 0;
}
