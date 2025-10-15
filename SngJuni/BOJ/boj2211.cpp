#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

int N, M;
vector<vector<pair<int, int>>> graph;
vector<int> dist;
vector<int> parent;

// 다익스트라 알고리즘
void dijkstra(int s) {
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.emplace(0, s);
    dist[s] = 0;

    while (!pq.empty()) {
        int cd = pq.top().first;   // 현재까지의 거리
        int cu = pq.top().second;  // 현재 정점
        pq.pop();

        if (cd > dist[cu]) continue;  // 더 긴 거리면 무시 
        for (const auto& i : graph[cu]) {
            int nd = cd + i.second;    // 현재 거리  + 간선 가중치
            if (dist[i.first] > nd) {  // 더 짧은 경로 발견
                dist[i.first] = nd;    // 거리 갱신
                parent[i.first] = cu;  // 부모 기록
                pq.emplace(nd, i.first);
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);  // 입출력 최적화 코드
    cin.tie(NULL);

    cin >> N >> M;
    graph.assign(N + 1, {});
    dist.assign(N + 1, INT_MAX);  // 다익스트라 알고리즘을 위한 최단거리의 초기값
    parent.assign(N + 1, -1);     // 각 간선의 부모 초기값

    int A, B, C;
    for (int i = 0; i < M; i++) {
        cin >> A >> B >> C;
        graph[A].push_back({B, C});
        graph[B].push_back({A, C});
    }

    dijkstra(1);  // 1번 컴퓨터에서 시작

    cout << N - 1 << '\n';  // 복구가 필요한 간선은 항상 N - 1개
    for (int i = 2; i <= N; i++) {
        cout << parent[i] << ' ' << i << '\n';  // 최단 경로의 부모-자식 출력
    }

    return 0;
}