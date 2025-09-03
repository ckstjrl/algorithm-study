#include <iostream>
#include <deque>
#include <cmath>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);  // 입출력 속도 최적화
    cin.tie(NULL);

    int n, x;
    cin >> n;

    deque<pair<int, int>> dq;  // deque 자료구조 사용
    for (int i = 1; i <= n; i++) {  // 풍선과 종이 pair 로 짝지어서 deque 에 push
        cin >> x;
        dq.push_back({i, x});
    }
    
    while (dq.size() > 1) {               // deque 에 마지막 하나가 남을 때까지
        cout << dq.front().first << " ";  // 터뜨린 풍선 출력
        int pos = dq.front().second;      // 다음 풍선 위치
        dq.pop_front();

        if (pos > 0) {  // 다음 풍선 위치가 양수일 경우
            for (int i = 0; i < pos - 1; i++) {  // pos - 1 만큼 deque 의 뒤로 이동
                dq.push_back(dq.front());
                dq.pop_front();
            }
        } else {        // 다음 풍선 위치가 음수일 경우
            for (int i = abs(pos); i >= 1; i--) {  // pos 만큼 deque 의 앞으로 이동
                dq.push_front(dq.back());
                dq.pop_back();
            }
        }
    }

    cout << dq.front().first << '\n';  // deque 에 남은 마지막 풍선 출력

    return 0;
}