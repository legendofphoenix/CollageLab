#include <bits/stdc++.h>
using namespace std;
int main()
{
int n;
cin >> n;
string s[n*2];
for (int i=0; i<n*2; i++)
cin >> s[i];
vector < pair<string,string> > sv;
for (int i=0; i<n*2; i+=2)
sv.push_back(make_pair(s[i],s[i+1]));
sort(sv.begin(),sv.end());
cout << "After sorting\nName ID\n";
for (int i=0; i<n; i++)
cout << sv[i].first << " " << sv[i].second << endl;
return 0;
}
