#include <iostream>
#include <vector>
#include <queue>
#include <climits>
#include <algorithm>

using namespace std;

int N, M, X;
vector<vector<pair<int, int>>> graph, rgraph;
vector<int> dist, rdist;

// 특정 정점에서 각 정점까지의 최단거리를 구하는 다익스트라 함수
void dijkstra(int start, const vector<vector<pair<int, int>>> &g, vector<int> &d) {  // 간선 정보과 최단거리 배열을 인수로 넣어줌.
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.emplace(0, start);
    d[start] = 0;

    while (!pq.empty()) {
        int cw = pq.top().first;
        int u = pq.top().second;
        pq.pop();

        if (cw > d[u]) continue;  // 이미 더 짧은 시간인 경우

        for (const auto& i : g[u]) {  // 인접리스트 순회하면서 최단거리 갱신
            int v = i.first;
            int w = i.second;

            if (cw + w < d[v]) {
                pq.emplace(cw + w, v);
                d[v] = cw + w;
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);  // 입출력 최적화 코드
    cin.tie(NULL);

    cin >> N >> M >> X;

    graph.assign(N + 1, {});      // X에서 돌아오는 도로를 위한 간선 정보
    rgraph.assign(N + 1, {});     // X로 가는 도로를 위한 간선 정보
    dist.assign(N + 1, INT_MAX);  // X에서 돌아오는 최단거리를 위한 거리 배열
    rdist.assign(N + 1, INT_MAX); // X로 가는 최단거리를 위한 거리 배열

    int s, e, t;
    for (int i = 0; i < M; i++) {  // 간선 정보를 받아서 2가지로 저장
        cin >> s >> e >> t;
        graph[s].push_back({e, t});
        rgraph[e].push_back({s, t});
    }

    dijkstra(X, graph, dist);   // X에서 각 정점으로 돌아오는 최단거리 계산

    dijkstra(X, rgraph, rdist); // 각 정점에서 X로 가는 최단거리 계산

    int res = 0;
    for (int i = 1; i <= N; i++) {
        if (dist[i] == INT_MAX || rdist[i] == INT_MAX) continue;  // 둘 중 하나라도 도달하지 못할 경우
        res = max(res, dist[i] + rdist[i]);  // 최대거리 갱신
    }

    cout << res << '\n';  // 결과 출력

    return 0;
}