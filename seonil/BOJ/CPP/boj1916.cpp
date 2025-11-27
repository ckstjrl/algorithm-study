/*
BOJ1916. 최소비용 구하기

[문제]
N개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스가 있다.
우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다.
A번째 도시에서 B번째 도시까지 가는데 드는 최소비용을 출력하여라. 도시의 번호는 1부터 N까지이다.

[입력]
첫째 줄에 도시의 개수 N(1 ≤ N ≤ 1,000)이 주어지고 둘째 줄에는 버스의 개수 M(1 ≤ M ≤ 100,000)이 주어진다.
그리고 셋째 줄부터 M+2줄까지 다음과 같은 버스의 정보가 주어진다.
먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다. 그리고 그 다음에는 도착지의 도시 번호가 주어지고 또 그 버스 비용이 주어진다. 버스 비용은 0보다 크거나 같고, 100,000보다 작은 정수이다.
그리고 M+3째 줄에는 우리가 구하고자 하는 구간 출발점의 도시번호와 도착점의 도시번호가 주어진다. 출발점에서 도착점을 갈 수 있는 경우만 입력으로 주어진다.

[출력]
첫째 줄에 출발 도시에서 도착 도시까지 가는데 드는 최소 비용을 출력한다.
*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;
const int INF = 1e9;

// 다익스트라 알고리즘 함수
int dijkstra(int start, int goal, const vector<vector<pair<int,int>>>& graph, int N) {
    
    // 다익스트라 준비
    vector<int> dist(N + 1, INF);   // 최단거리 테이블 초기화
    dist[start] = 0;    // 출발 도시는 비용 0

    // 우선순위 큐를 사용하여 가장 비용이 작은 도시부터 처리
    priority_queue<
        pair<int,int>,
        vector<pair<int,int>>,
        greater<pair<int,int>>  // pair<비용, 도시번호>이므로 비용 기준 오름차순 정렬
    > pq;

    pq.push({0, start});    // 출발 도시 추가

    while (!pq.empty()) {
        auto [currentDist, node] = pq.top();    // 현재 탐색할 비용, 도시번호
        pq.pop();

        // 이미 더 짧은 경로를 찾았으면 넘어감
        if (currentDist > dist[node]) continue;

        // 현재 도시에서 갈 수 있는 모든 인접 도시 확인
        for (auto [next, cost] : graph[node]) {
            int nextDist = currentDist + cost;  // nextDist: 현재 도시를 거쳐서 가는 비용
            
            // 현재 도시를 거쳐서 가는 비용이 최단거리 테이블의 기록보다 작으면 갱신하고 큐에 추가
            if (nextDist < dist[next]) {
                dist[next] = nextDist;
                pq.push({nextDist, next});
            }
        }
    }
    // 목표 도시까지의 최소 비용 반환
    return dist[goal];
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N; // N: 도시의 개수(노드의 개수)
    cin >> M; // M: 버스의 개수(간선의 개수)

    // 간선 정보 입력 받기
    vector<vector<int>> edges(M, vector<int>(3, 0));
    for (int i = 0; i < M; i++) {
        cin >> edges[i][0] >> edges[i][1] >> edges[i][2];
    }
  
    // 간선 정보를 인접 리스트로 변환
    vector<vector<pair<int, int>>> graph(N + 1);
    int s, e, cost;
    for (int i = 0; i < M; i++) {
        int s = edges[i][0];
        int e = edges[i][1];
        int cost = edges[i][2];
        graph[s].push_back({e, cost});
    }
    // 구간 출발점의 도시번호와 도착점의 도시번호 입력 받기
    int start, goal;
    cin >> start >> goal;

    // 다익스트라 실행
    int result = dijkstra(start, goal, graph, N);

    // 결과 출력
    if (result == INF) cout << "-1\n";  // 도달 불가 시 -1 출력(사실 이 문제에서는 필요 없지만 형식적으로 만들어 놓기)
    else cout << result << "\n";    // 도달 가능하면 최소 비용 출력

    return 0;
}