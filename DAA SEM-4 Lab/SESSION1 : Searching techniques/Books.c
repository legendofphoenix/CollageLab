#include <stdio.h>
int main()
{
int n, a[10], i, flag = 0;
scanf("%d",&n);
for(i=0; i<n; i++)
{
scanf("%d",&a[i]);
if(a[i] == 195)
flag = 1;
}
if(flag)
printf("Book Available");
else
printf("Book is not available");
return 0;
}
