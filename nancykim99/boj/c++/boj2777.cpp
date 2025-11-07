// BOJ2777 : 숫자놀이 (S2)
// 해결 방법 : 9부터 2까지 그리디기법으로 나누면서, 나눠지면, 자릿수 추가하고, 안 된다면 -1을 출력하기

#include <iostream>
using namespace std;

int main() {
  int tc;
  cin >> tc;
  for (int i = 0; i < tc; i++) {
    int n;
    cin >> n;
    int ans = 0;
    if (n == 1) {
      ans = 1;
    } else {
      while (true) {
        if (n < 10) {
          ans += 1;
          break;
        }
        int flag = 0;
        for (int d = 9; d > 1; d--) {
          if ((n % d) == 0) {
            n /= d;
            ans += 1;
            flag = 1;
            break;
          }
        }
        if ((flag == 0) && (n >= 10)) {
          ans = -1;
          break;
        }
      }
    }
    cout << ans << '\n';  
  }
  return 0;
}