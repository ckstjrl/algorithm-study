/*
BOJ2075 : N번째 큰 수 (S3)

해결 방법 : 한 줄씩 돌아가면서, 힙큐 최소값과 비교하는 방법으로 다섯번째로 작은 숫자 구하기 (n번째로 작은 숫자)

메모 : c++로 시간 초과 피하는 방법이 복잡하다!
*/

/* 시간 초과난 코드...
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<vector<int>> num_arr(n, vector<int>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> num_arr[i][j];
        }
    }

    priority_queue<int, vector<int>, greater<int>> pq;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if ((int)pq.size() < n) {
                pq.push(num_arr[i][j]);
            }
            else if (pq.top() < num_arr[i][j]) {
                pq.pop();
                pq.push(num_arr[i][j]);
            }
        }
    }

    cout << pq.top() << '\n';
    return 0;
}
*/

#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    priority_queue<int, vector<int>, greater<int>> pq;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int x;
            cin >> x;
            if ((int)pq.size() < n) pq.push(x);
            else if (pq.top() < x) {
                pq.pop();
                pq.push(x);
            }
        }
    }

    cout << pq.top() << '\n';
    return 0;
}
