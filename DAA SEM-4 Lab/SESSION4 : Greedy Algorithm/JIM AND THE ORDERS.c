#include <stdio.h>
int main()
{
int n, t[10], d[10], sum[10], lol[10], i, j, temp;
scanf("%d",&n);
for(i=0; i<n; i++)
{
scanf("%d %d",&t[i],&d[i]);
sum[i] = t[i] + d[i];
lol[i] = sum[i];
}
for(i=0; i<n-1; i++)
for(j=i+1; j<n; j++)
if(lol[i] > lol[j])
{
temp = lol[i]; lol[i] = lol[j]; lol[j] = temp;
}
for(i=0; i<n; i++)
for(j=0; j<n; j++)
if(lol[i] == sum[j])
{
printf("%d ",j+1);
sum[j] = 0;
}
return 0;
}
