#include <iostream>
using namespace std;
int main()
{
int n; cin>>n;
int a[10];
for(int i=0; i<n; i++) cin>>a[i];
int ans = 0 , i;
for(i=0; i<n/2; i++)
{
ans += abs(a[i]-a[n-i-1]);
ans += abs(a[i+1]-a[n-i-1]);
}
ans += abs(a[0]-a[i]);
cout<<ans;
return 0;
}
