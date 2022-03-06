#include <iostream>
using namespace std;
int main()
{
int n;
cin >> n;
string s[n];
long long int num[n];
int year[n];
for(int i=0; i<n; i++)
cin >> s[i] >> num[i] >> year[i];
string x;
cin >> x;
int flag = -1;
for(int i=0; i<n; i++)
if(s[i] == x)
flag = i;
if (flag != -1)
cout << "Name TelephoneNumber Year" << endl << s[flag] << " "
<< num[flag] << " " << year[flag];
else
cout << "The Entered Name is not in the Directory";
return 0;
}
