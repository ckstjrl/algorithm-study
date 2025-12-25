#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int N, M, K;
    cin >> N >> M >> K;

    vector<vector<pair<long long, int>>> graph(N + 1);  // a에서 b까지의 거리 c 정보를 담는 인접 리스트
    int a, b, c;
    for (int i = 0; i < M; i++) {
        cin >> a >> b >> c;
        graph[a].push_back({c, b});
    }

    // i번 도시까지의 경로들 중 짧은 거리들을 k개 저장
    // 최대힙 사용해서 가장 큰 값(top)이 k번째 최단거리
    vector<priority_queue<long long>> dist(N + 1);

    // 우선순위 큐 (min_heaP) : (현재까지 비용, 현재 도시)
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
    pq.push({0, 1});  // 1번 도시 초기화
    dist[1].push(0);

    // Dijkstra 탐색
    while (!pq.empty()) {
        long long cost = pq.top().first;  // 현재 누적 거리
        int cur = pq.top().second;        // 현재 도시
        pq.pop();

        // 인접 도시 탐색
        for (auto& g : graph[cur]) {
            long long nxtCost = g.first;    // 다음 간선 비용
            int nxt = g.second;             // 다음 도시
            long long nc = cost + nxtCost;  // 새 누적 거리

            // K개보다 적게 저장되어 있으면 무조건 추가
            if (dist[nxt].size() < K) {
                dist[nxt].push(nc);
                pq.push({nc, nxt});
            }
            // K개 들어있지만, 현재 경로가 더 짧을 경우 교체
            else if (dist[nxt].top() > nc) {
                dist[nxt].pop();
                dist[nxt].push(nc);
                pq.push({nc, nxt});
            }
        }
    }

    // 결과 출력
    for (int i = 1; i <= N; i++) {
        if (dist[i].size() < K) {
            cout << -1 << '\n';
        }
        else {
            cout << dist[i].top() << '\n';
        }
    }

    return 0;
}