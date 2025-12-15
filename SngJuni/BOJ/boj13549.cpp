#include <iostream>
#include <deque>
#include <vector>

using namespace std;

const int MAX = 100000;
const int INF = 1e9;

int bfs(int start, int target) {
    vector<int> dist(MAX + 1, INF);
    deque<int> dq;

    dist[start] = 0;
    dq.push_back(start);

    while (!dq.empty()) {
        int x = dq.front();
        dq.pop_front();

        if (x == target) {
            return dist[x];   // 최단 거리 도착
        }

        // 0초 이동: 순간이동
        int nx = x * 2;
        if (nx <= MAX && dist[nx] > dist[x]) {
            dist[nx] = dist[x];
            dq.push_front(nx);
        }

        // 1초 이동: x - 1
        nx = x - 1;
        if (nx >= 0 && dist[nx] > dist[x] + 1) {
            dist[nx] = dist[x] + 1;
            dq.push_back(nx);
        }

        // 1초 이동: x + 1
        nx = x + 1;
        if (nx <= MAX && dist[nx] > dist[x] + 1) {
            dist[nx] = dist[x] + 1;
            dq.push_back(nx);
        }
    }

    return dist[target];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, K;
    cin >> N >> K;

    cout << bfs(N, K) << '\n';

    return 0;
}
