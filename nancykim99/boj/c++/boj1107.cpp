/*
BOJ1107 : 리모컨 (G4)

해결 방법 : 
1. 숫자 버튼 안 쓰고 +, - 만 사용하기
2. 누를 수 있는 버튼들로 중복 순열 만들어서 다 시도해보기
*/

#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int goal;
    int n;
    cin >> goal >> n;

    vector<bool> broken(10, false);
    for (int i = 0; i < n; i++) {
        int a;
        cin >> a;
        broken[a] = true;
    }

    int answer = abs(goal - 100);  

    for (int ch = 0; ch <= 1000000; ch++) {
        int x = ch;

        int len = 0;
        if (x == 0) {
            if (broken[0]) continue;
            len = 1;
        } else {
            bool ok = true;
            while (x > 0) {
                int d = x % 10;
                if (broken[d]) {
                    ok = false;
                    break;
                }
                x /= 10;
                len++;
            }
            if (!ok) continue;
        }

        int press = len + abs(ch - goal);
        if (press < answer) answer = press;
    }

    cout << answer;
    return 0;
}

