#include <iostream>
#include <vector>
#include <queue>

#define INF 987654321

using namespace std;

int N, M;
vector<pair<int, int>> graph[1001];
int distArr[1001];
int s, e;

void dijkstra() {
    // (현재 비용, 노드)
    priority_queue<
        pair<int,int>,
        vector<pair<int,int>>,
        greater<pair<int,int>>
    > pq;

    // dist 배열 초기화
    for (int i = 1; i <= N; i++) {
        distArr[i] = INF;
    }

    distArr[s] = 0;
    pq.push({0, s});    // 시작 비용 0, 시작 노드 s

    while (!pq.empty()) {
        int cost = pq.top().first;
        int cur  = pq.top().second;
        pq.pop();

        if (distArr[cur] < cost) continue;

        for (auto &nx : graph[cur]) {
            int next = nx.first;
            int nd   = cost + nx.second;

            if (nd < distArr[next]) {
                distArr[next] = nd;
                pq.push({nd, next});
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> N >> M;

    for (int i = 0; i < M; i++) {
        int a, b, w;
        cin >> a >> b >> w;
        graph[a].push_back({b, w});
    }

    cin >> s >> e;

    dijkstra();

    cout << distArr[e];

    return 0;
}
