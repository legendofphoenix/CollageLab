#include <iostream>
using namespace std;
long long int ans[] = { -1 , -1 , -1 ,
555 , -1 , 33333 , 555555 , -1 , 55533333 , 555555555 ,
3333333333 , 55555533333 ,
555555555555 , 5553333333333 ,
55555555533333 , 555555555555555 };
int main()
{
int n;
cin>>n;
while(n--)
{
int a; cin >> a;
cout << ans[a] << endl;
}
return 0;
}
