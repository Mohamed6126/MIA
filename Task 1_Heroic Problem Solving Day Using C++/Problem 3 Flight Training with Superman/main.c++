#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin >> n;
    int a[n];
    int i=0,m=0;
    while(i++<n) {
    cin >> a[i];
    if(m<a[i]) m=a[i];
    }
    cout << m << endl;
    return 0;
}
