#include <stdio.h>
int MAX(int a,int b,int c)
{ if(a>=b) { if(a>=c) return a; return c; } else if(b>=c) return b; return
c; }
int MIN(int a,int b,int c)
{ if(a<=b) { if(a<=c) return a; return c; } else if(b<=c) return b; return
c; }
int main()
{
int r,g,b;
scanf("%d%d%d",&r,&g,&b);
int max = MAX(r,g,b) , min = MIN(r,g,b);
int mid;
if(r!=max && r!=min) mid = r;
else if(g!=max && g!=min) mid = g;
else mid = b;
int ans = mid +1 + (max-mid)/2;
printf("%d",ans);
return 0;
}
