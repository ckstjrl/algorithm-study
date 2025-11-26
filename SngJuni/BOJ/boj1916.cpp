#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

int N, M, s, d;
vector<vector<pair<int, int>>> graph;
vector<int> dist;  // 시작점에서 각 정점까지의 최소 거리

void djikstra(int start, int dest) {
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, start});  // 출발점 0으로 초기화
    dist[start] = 0;

    while (!pq.empty()) {
        int cw = pq.top().first;
        int cur = pq.top().second;
        pq.pop();

        if (cw > dist[cur]) continue;  // 현재 비용보다 더 크면 스킵 (가지치기)

        for (auto& i : graph[cur]) {
            int nxt = i.first;
            int nw = i.second;

            if (dist[nxt] > cw + nw) {
                dist[nxt] = cw + nw;
                pq.push({dist[nxt], nxt});
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> M;

    graph.assign(N + 1, {});
    dist.assign(N + 1, INT_MAX);

    int u, v, w;
    for (int i = 0; i < M; i++) {
        cin >> u >> v >> w;
        graph[u].push_back({v, w});  // 인접리스트로 그래프 구현
    }

    cin >> s >> d;

    djikstra(s, d);  // 출발점에서부터 도착점까지 다익스트라

    cout << dist[d] << '\n';

    return 0;
}