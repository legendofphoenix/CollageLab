#include <bits/stdc++.h>
using namespace std;
int main()
{
int t; cin>>t;
while(t--)
{
int n , a[10] , b[10];
cin>>n;
for(int i=0; i<n; i++)
cin>>a[i];
for(int i=0; i<n; i++)
cin>>b[i];
sort(a,a+n);
sort(b,b+n,greater<int>());
int ans = 0;
for(int i=0; i<n; i++)
if(a[i]%b[i]==0 || b[i]%a[i]==0)
ans += 1;
cout << ans << endl;
}
return 0;
}
