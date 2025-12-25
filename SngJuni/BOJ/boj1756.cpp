#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int D, N;
    cin >> D >> N;

    vector<int> oven(D);  // 오븐 지름 배열
    for (int i = 0; i < D; i++) {
        cin >> oven[i];
    }

    vector<int> pizza(N);  // 피자 지름 배열
    for (int i = 0; i < N; i++) {
        cin >> pizza[i];
    }
    
    for (int i = 1; i < D; i++) {  // 오븐 지름 위에서부터 작은 값을 선택하도록
        oven[i] = min(oven[i], oven[i - 1]);
    }

    int res = -1;      // 마지막으로 피자가 들어간 위치
    int pos = D - 1;   // 현재 탐색할 깊이
    bool flag = false;

    for (int i = 0; i < N; i++) {
        while (pos >= 0 && oven[pos] < pizza[i]) {
            pos--;  // 이 깊이에는 피자가 못 넣으므로 한 칸 위로 이동
        }

        if (pos < 0) {  // 더 이상 들어갈 자리 없음
            flag = true;
            break;
        }

        res = pos;  // pos에 i번째 피자 들어감
        pos--;      // 한 칸 위로 이동
    }

    if (flag) {
        cout << 0 << '\n';
    } else {
        cout << res + 1 << '\n';  // 0-based 여서 1 더해서 출력
    }

    return 0;
}