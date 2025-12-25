/*** 2211. 네트워크 복구 ***/

#include<iostream>
#include<vector>
#include<queue>
#include<climits>
using namespace std;

void dijkstra(int start_node);

vector<vector<pair<int, int>>> graph;
vector<int> dists;
vector<int> path; // 경로 추적을 위한 배열
int N, M;

int main() {
	cin >> N >> M;
	graph.assign(N + 1, {});
	dists.assign(N + 1, INT_MAX);
	path.assign(N + 1, -1);
	for (int i = 0; i < M; i++) {
		int u, v, w;
		cin >> u >> v >> w;
		graph[u].push_back({ w, v }); // 쌍방향이라고 했으므로 양방향 모두 인접 리스트 저장
		graph[v].push_back({ w, u });
	}
	
	dijkstra(1); // 1번에서 최단경로 찾기

	cout << N - 1 << '\n';
	for (int i = 2; i < N + 1; i++) { // 무조건 모든 노드를 잇고, 1은 루트 노드이므로 2부터 N까지 순회
		cout << path[i] << ' ' << i << '\n';
	}

	return 0;
}

void dijkstra(int start_node) {
	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
	pq.push({ 0, start_node });
	dists[start_node] = 0;

	while (!pq.empty()) {
		int dist = pq.top().first;
		int node = pq.top().second;
		pq.pop();

		if (dists[node] < dist) continue;

		for (const auto& x : graph[node]) {
			int next_dist = x.first;
			int next_node = x.second;
			int new_dist = dist + next_dist;

			if (dists[next_node] <= new_dist) continue;

			dists[next_node] = new_dist;
			path[next_node] = node; // 다음 노드의 경로 배열에 현재 노드 저장 
			pq.push({ new_dist, next_node });
		}
	}
}