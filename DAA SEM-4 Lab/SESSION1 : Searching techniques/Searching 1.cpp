#include <iostream>
using namespace std;
int main()
{
  int x, y, z, a[10], b[10], c[10], i, j, k;
cin>>x; for(i=0; i<x; i++) cin>>a[i];
cin>>y; for(i=0; i<y; i++) cin>>b[i];
cin>>z; for(i=0; i<z; i++) cin>>c[i];
int d1=1000, d2=1000, d3=1000, i1=0, j1=0, k1=0; float avg=1000;
for(i=0; i<x; i++) for(j=0; j<y; j++) for(k=0; k<z; k++)
{
int td1 = abs(a[i]-b[j]) , td2 = abs(b[j]-c[k]) , td3 = abs(c[k]-a[i]);
float tavg = (td1+td2+td3)/3.0;
if( (td1<d1 && td2<d2 || td3<d3) && tavg<avg )
{
d1 = td1; d2 = td2; d3 = td3;
avg = (d1+d2+d3)/3.0;
i1 = i; j1 = j; k1 = k;
}
}
cout << a[i1] << " " << b[j1] << " " << c[k1];
return 0;
}
