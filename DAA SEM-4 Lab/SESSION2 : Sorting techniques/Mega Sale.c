#include <stdio.h>
int main()
{
int t;
scanf("%d",&t);
while(t--)
{
int n,m,a[100],i,j,temp,ans=0;
scanf("%d%d",&n,&m);
for(i=0; i<n; i++)
scanf("%d",&a[i]);
for(i=0; i<n-1; i++)
for(j=i+1; j<n; j++)
if(a[i]>a[j]) { temp=a[i]; a[i]=a[j]; a[j]=temp; }
for(i=0; i<n; i++)
{
if(a[i]<0)
{
ans-=a[i];
m-=1;
}
if(m==0) break;
}
printf("%d\n",ans);
}
return 0;
}
