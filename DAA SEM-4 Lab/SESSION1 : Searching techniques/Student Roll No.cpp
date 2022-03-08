#include <iostream>
using namespace std;
int main()
{
int i=-1 , a[20] , n , temp=0;
while (cin>>n)
{
a[++i] = n;
if (n==5) temp=1;
}
for ( ; i>=0; i--)
for ( int j=i-1; j>=0; j--)
if ( a[i] < a[j] )
{
int t = a[i];
a[i] = a[j];
a[j] = t;
}
i = 0;
cout << "Sorted Rollnumber list is\n";
while (a[i])
cout << a[i++] << " ";
if (temp)
cout << "\nRoll no 5 belongs to the list";
else
cout << "\nRoll no 5 does not belong to the list";
return 0;
}
