#include <iostream>
#include <deque>

using namespace std;

int main() {
    int n;
    cin >> n;
    
    deque<int> dq;  // 자료구조 deque를 사용
    for (int i = 1; i <= n; i++) {  // 1부터 N까지의 숫자를 dq에 넣음.
        dq.push_back(i);
    }

    while (dq.size() > 1) {        // dq에서 끝 값 하나를 남길 때까지 반복
        cout << dq.front() << " "; // 버린 카드 출력
        dq.pop_front();            // 제일 위의 카드를 바닥에 버림.
        dq.push_back(dq.front());  // 제일 위의 카드를 제일 아래로 옮김.
        dq.pop_front();
    }
    
    cout << dq.front() << '\n';    // 마지막에 남은 카드 출력

    return 0;
}