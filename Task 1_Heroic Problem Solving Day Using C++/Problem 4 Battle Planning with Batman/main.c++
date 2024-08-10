#include <bits/stdc++.h>
using namespace std;
int main()
{
    int r,c,v=0,h=0;
    cin >> r >> c;
    int a[r][c],b[r][c];
    for(int i=0;i<r;i++)
    for(int j=0;j<c;j++) cin >> a[i][j];
    for(int m=0;m<r;m++)
    for(int k=0;k<c;k++) {
     cin >> b[m][k];
    if(a[m][k]<b[m][k])v++;
    else if(a[m][k]>b[m][k])h++;
    }
    if(v>h) cout << "Villains" << endl;
    else if (v<h) cout << "Justice League" << endl;
    else cout << "Tie" << endl;
    return 0;
}