#include <bits/stdc++.h>

using namespace std;

int main() 

{

  int n,i=0,flag;

  cin >> n;

  int a[n];

  while(i++<n) cin >> a[i];

  int key,index=0;

  cin >> key;

  while(index<=n){

    if(key==a[index]){

    flag= 1;

    break;

  }

  else flag=-1;

  index++;

  }

  if (flag>0) cout << --index;

  else cout << flag;

    return 0;

}