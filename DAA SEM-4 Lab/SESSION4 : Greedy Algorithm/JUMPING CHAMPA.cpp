#include <iostream>
using namespace std;
int main()
{
int t; cin>>t;
while(t--)
{
int n, q, a[10], i, ans = 0;
cin>>n>>q;
for(i=0; i<n; i++) cin>>a[i];
for(i=0; i<n-1; i++)
ans += q*abs(a[i+1]-a[i]);
cout << ans << endl;
}
return 0;
}
