#include <bits/stdc++.h>
using namespace std;
int main()
{
int t;
cin>>t;
while(t--)
{
int n; cin>>n;
int a[n] , i;
for(i=0; i<n; i++)
cin >> a[i];
sort (a, a+n);
int res = 1;
for(i=1; i<n; i++)
if(a[i]-a[i-1] != 1)
res++;
cout << res<< endl;
}
return 0;
}
