/*
BOJ1916 : 최소비용 구하기 (G5)

해결 방법 : 
출발 정류장부터 도착 정류장까지 최소 비용 (= 경로) -> 다익스트라
모든 정류장을 잇는 것이 아니기에, MST가 아님
1. 인접리스트 구하기 : 도착 지점, weight
3. 시작 정류장부터 모든 정류장의 최소 비용 다익스트라로 구하기
  3-1. 무한대로 거리 배열 만들기
  3-2. 시작 정류장 == 0
  3-3. weight 기준으로 정렬하기
  3-4. 우선순위큐가 있는 동안
  3-5. 현재 거리가 최종 거리보다 같거나 크면 버리기
  3-6. 모든 인접 노드들을 돌며, 현재까지의 거리 + 거리가 기존보다 작으면 갱신
  3-7. 갱신한 값 큐에 업데이트

메모 : 

- 우선순위큐에 거리 노드 넣기
'''
priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
'''

- C++ 함수 선언에서는 모든 매개변수에 타입을 명시
'''
int dijkstra(const vector<vector<pair<int,int>>>& graph, int start_node, int end_node)
'''

- 최대수로 만들어진 거리 배열
'''
const int INF = 1e9;
vector<int> dist(n + 1, INF);
'''

- pq가 비었을 때
'''
while (!pq.empty()) {}
'''

- c++은 pop 시, pop 된 값을 반환하지 않음
'''
auto [current_dist, current_node] = pq.top();
pq.pop();
'''

- c++ 튜플 언팩하기
'''
for (auto &p : graph[current_node]) {
    int next = p.first;
    int weight = p.second;
}
'''
*/

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

const int INF = 1e9;

int n, m;
int a, b, w;
int x, y;

int dijkstra(const vector<vector<pair<int,int>>>& graph, int start_node, int end_node) {
    // 거리 배열 초기화하기
    vector<int> dist(n + 1, INF);

    // (거리, 노드) 기준 최소 힙
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;

    dist[start_node] = 0;
    pq.push({0, start_node});
    while (!pq.empty()) {
        auto [current_dist, current_node] = pq.top();
        pq.pop();
        // 이미 더 짧은 경로가 있으면 skip
        if (current_dist > dist[current_node]) continue;
        for (auto [next, weight] : graph[current_node]) {
            int ndist = current_dist + weight;
            if (ndist < dist[next]) {
                dist[next] = ndist;
                pq.push({ndist, next});
            }
        }
    }

    return dist[end_node];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> m;
    // n 크기를 입력받은 뒤에 인접 리스트 크기 설정
    vector<vector<pair<int,int>>> graph(n + 1);
    // 인접 리스트 입력 : 단방향
    for (int i = 0; i < m; i++) {
        cin >> a >> b >> w;
        graph[a].push_back({b, w});
    }
    cin >> x >> y;
    int ans = dijkstra(graph, x, y);
    cout << ans << '\n';
    return 0;
}
