/*
BOJ11729 : 하노이 탑 이동 순서 (G5)

해결 방법 : 
거꾸로 푼다고 생각하면 쉬움
재귀로 돌면서, 맨 위 반, 중간, 맨 아래 반 이렇게 진행 순서를 나눠서 재귀
*/

#include <iostream>
#include <vector>
#include <tuple>
using namespace std;

vector<pair<int, int>>moved;

void moving(int n, int s, int e, int h) {
  if (n == 0) {
    return;
  }
  moving(n-1, s, h, e);
  cout << s << " " << e << '\n';
  moving(n-1, h, e, s);
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  long long ans = (1LL << n) - 1; 
  cout << ans << '\n';
  moving(n, 1, 3, 2);
  return 0;
}