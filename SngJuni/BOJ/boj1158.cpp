#include <iostream>
#include <queue>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);  // 입출력 속도 최적화 코드
    cin.tie(NULL);

    int n, k;
    cin >> n >> k;
    
    queue<int> q;  // 자료구조 queue 사용
    for (int i = 1; i <= n; i++) {
        q.push(i);
    }

    cout << '<';
    while (q.size() > 1) {  // queue에서 마지막 사람 1명이 남을 때까지 반복
        for (int i = 0; i < k - 1; i++) {  // K - 1명을 queue의 맨뒤로 이동
            q.push(q.front());
            q.pop();
        }
        cout << q.front() << ", ";  
        q.pop();  // K번째 사람 제거
    }
    cout << q.front() << ">\n";  // 마지막 사람 제거

    return 0;
}