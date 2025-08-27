#include <iostream>
#include <queue>

using namespace std;

int n, k;
int res[100001];  // 각 점까지 걸리는 시간을 위한 정적 배열

int bfs(int i) {
    queue<int> q;
    q.push(i);
    res[i] = 1;

    while (!q.empty()) {
        int cur = q.front();
        q.pop();

        // 동생을 찾으면 해당 시간을 반환하고 종료
        if (cur == k) {
            return res[cur] - 1;
        }

        // X - 1 로 이동
        if (cur - 1 >= 0 && res[cur - 1] == 0) {
            q.push(cur - 1);
            res[cur - 1] = res[cur] + 1;
        }

        // X + 1 로 이동
        if (cur + 1 < 100001 && res[cur + 1] == 0) {
            q.push(cur + 1);
            res[cur + 1] = res[cur] + 1;
        }

        // 2 * X 로 이동
        if (cur * 2 < 100001 && res[cur * 2] == 0) {
            q.push(cur * 2);
            res[cur * 2] = res[cur] + 1;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> k;

    int res = bfs(n);     // bfs를 통해 탐색
    cout << res << '\n';

    return 0;
}