#include <iostream>
#include <string.h>
using namespace std;
int main()
{
int t;
cin>>t;
while(t--)
{
char a[20];
cin >> a;
for(int i=0; i<strlen(a); i++)
if(a[i-1] != a[i])
cout<<a[i];
cout<<endl;
}
return 0;
}
