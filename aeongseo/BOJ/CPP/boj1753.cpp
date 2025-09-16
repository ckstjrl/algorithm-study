/*** 1753. 최단경로 ***/

#include<iostream>
#include<vector>
#include<queue>
#define INF 1000000000
using namespace std;

void dijkstra(int start_node);

vector<pair<int, int>> graph[20001];
vector<int> dists;
int V, E, start;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> V >> E >> start;

	for (int i = 0; i < E; i++) {
		int u, v, w;
		cin >> u >> v >> w;
		graph[u].push_back({ w, v });    // 인접 리스트에 가중치, 도착 노드 저장
	}

	dijkstra(start);

	for (int j = 1; j < V+1; j++) {
		if (dists[j] == INF) {    // 노드에 도착 못했으면 INF 출력
			cout << "INF" << '\n';
		}
		else {
			cout << dists[j] << '\n';    // 도착했으면 거리 출력
		}
	}

	return 0;
}

void dijkstra(int start_node) {
	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
	pq.push({ 0, start_node });    // 시작지점이므로 가중치 0과 시작노드 저장
	dists.assign(V + 1, INF);   // 거리 저장하기 위한 배열 INF로 초기화
	dists[start_node] = 0;    // 시작 노드의 거리 0 저장

	while (!pq.empty()) {
		int dist = pq.top().first;
		int node = pq.top().second;
		pq.pop();

		if (dists[node] < dist) continue;  // 이미 방문한 적 있다면 패스

		for (const auto& x : graph[node]) {    // 인접 노드 확인
			int next_dist = x.first;
			int next_node = x.second;
			int new_dist = dist + next_dist;    // 누적 거리

			if (dists[next_node] <= new_dist) continue;   // 현재 노드의 누적합이 기존에 저장된 누적합 거리보다 크거나 같으면 패스

			dists[next_node] = new_dist;    // 기존 누적합 거리보다 작으면 갱신 후 우선순위큐에 저장
			pq.push({ new_dist, next_node });
		}
	}
}