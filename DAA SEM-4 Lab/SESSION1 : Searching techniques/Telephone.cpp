#include <bits/stdc++.h>
using namespace std;
int main()
{
int n;
cin >> n;
string s[n];
long long int num[n];
for (int i=0; i<n; i++)
cin >> s[i] >> num[i];
long long int search;
cin >> search;
int flag = -1;
for(int i=0; i<n; i++)
if(num[i] == search)
flag = i;
vector < pair<string,long long int> > sv;
for (int i=0; i<n; i++)
sv.push_back(make_pair(s[i],num[i]));
sort(sv.begin(),sv.end());
cout << "Ordered List\n";
for (int i=0; i<n; i++)
cout << sv[i].first << " " << sv[i].second << endl;
cout << "\nName Telephone Number" << endl;
if(flag != -1)
cout << s[flag] << " " << num[flag];
else
cout << "The Entered Number is not in the Directory";
return 0;
  }
