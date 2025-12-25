/*** 1238. 파티 ***/

#include<iostream>
#include<vector>
#include<queue>
#include<climits>
#include<algorithm>
using namespace std;

// 인접리스트 생성
// X부터 다익스트라 -> 모든 dists 배열의 값을 해당 인덱스의 소요시간 배열에 더함
// 모두의 마을에서 X까지 다익스트라 -> 각 인덱스의 소요시간 배열에 값 더함

void dijkstra(int start);

vector<vector<pair<int, int>>> graph;
vector<int> dists;
vector<int> spend;	// X에 갔다 자신의 마을로 돌아오는 데의 소요시간 배열
int N, M, X;

int main() {
	cin >> N >> M >> X;
	graph.assign(N+1, {});
	dists.assign(N+1, INT_MAX);
	spend.assign(N+1, 0);

	for (int i = 0; i < M; i++) {
		int u, v, w;
		cin >> u >> v >> w;
		graph[u].push_back({ w, v });	// 단방향 도로
	}

	dijkstra(X);
	for (int i = 1; i < N + 1; i++) {	// X에서 자신의 마을들로 돌아가는 최단경로 값을 소요시간에 더함
		spend[i] += dists[i];
	}

	for (int i = 1; i < N + 1; i++) {	// 각 마을에서 X까지의 최단경로 값을 소요시간에 더함
		dists.assign(N + 1, INT_MAX);
		dijkstra(i); 
		spend[i] += dists[X];
	}

	int max_spend = 0;
	for (int i = 1; i < N + 1; i++) {	// 최대 소요시간 저장
		max_spend = max(max_spend, spend[i]);
	}

	cout << max_spend;

	return 0;
}

void dijkstra(int start) {
	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
	pq.push({ 0, start });
	dists[start] = 0;

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
			pq.push({ new_dist, next_node });
		}
	}
}