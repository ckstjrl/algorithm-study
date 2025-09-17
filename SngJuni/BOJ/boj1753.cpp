#include <iostream>
#include <vector>
#include <functional>
#include <queue>
#include <climits>

using namespace std;

int V, E, K;  // 정점, 간선, 시작 정점
vector<vector<pair<int, int>>> arr;  // 인접리스트로 방향그래프 정보 저장을 위한 2차원 가변배열
vector<int> dist;  // 시작 정점으로부터 각 정점까지의 최단거리를 위한 1차원 가변배열

void dijkstra(int start) {  // 다익스트라 알고리즘 함수
    // (거리, 정점) 쌍을 오름차순으로 꺼내는 최소 힙(우선순위 큐)
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, start});  // 시작 정점까지의 거리는 0으로 초기화하고 push
    dist[start] = 0;      // 시작 정점의 최단 거리 0으로 저장

    while (!pq.empty()) {
        int x = pq.top().first;   // 현재 큐에서 꺼낸 경로의 거리
        int u = pq.top().second;  // 현재 탐색할 정점
        pq.pop();

        for (const auto& i : arr[u]) {  // u에서 갈 수 있는 모든 정점 순회
            int v = i.first;   // 인접 정점 번호
            int w = i.second;  // 그 정점까지의 가중치

            if (x + w < dist[v]) {  // 현재 경로 x + w 가 dist[v] 보다 짧으면 갱신
                pq.push({x + w, v});
                dist[v] = x + w;
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);  // 입출력 최적화 코드
    cin.tie(NULL);

    cin >> V >> E >> K;

    arr.assign(V + 1, {});  // 인접리스트 초기화
    dist.assign(V + 1, INT_MAX);  // 모든 정점으로의 최단거리를 INT_MAX로 초기화

    int u, v, w;
    for (int i = 0; i < E; i++) {
        cin >> u >> v >> w;
        arr[u].push_back({v, w});  // u에서 v로 가는 간선의 가중치 w를 인접리스트에 저장
    }

    dijkstra(K);  // 다익스트라 함수 호출

    for (int i = 1; i <= V; i++) {
        if (dist[i] == INT_MAX) cout << "INF\n";  // 도착 불가능
        else cout << dist[i] << '\n';  // 도착 가능하면 최단 거리 출력
    }

    return 0;
}