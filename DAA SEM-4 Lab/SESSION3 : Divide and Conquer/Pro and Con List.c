#include <stdio.h>
int main()
{
int t;
scanf("%d",&t);
while(t--)
{
int n, a[10], b[10], i, j, k, temp, ans = 0;
scanf("%d",&n);
for(i=0; i<n; i++)
scanf("%d%d",&a[i],&b[i]);
for(i=0; i<n-1; i++)
for(j=i+1; j<n; j++)
{
temp = a[i] + a[j];
for(k=0; k<n; k++)
if(k!=i && k!=j)
temp -= b[k];
if (temp > ans)
ans = temp;
}
printf("%d\n",ans);
}
return 0;
}
