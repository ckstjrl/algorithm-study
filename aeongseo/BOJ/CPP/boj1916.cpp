/*** 1916. 최소비용 구하기 ***/

#include<iostream>
#include<queue>
#include<vector>
using namespace std;

const long long INF = 1e18;
int N, M, A, B;
vector<pair<int, int>> graph[1001];
vector<long long> dists;

void dijkstra(int start);

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> N >> M;

	for (int i = 0; i < M; i++) {
		int u, v, w;
		cin >> u >> v >> w;
		graph[u].push_back({ w, v });
	}

	cin >> A >> B;

	dijkstra(A);

	cout << dists[B];

	return 0;
}

void dijkstra(int start) {
	priority_queue < pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;

	pq.push({ 0, start });
	dists.assign(N + 1, INF);
	dists[start] = 0;

	while (!pq.empty()) {
		auto [cur_dist, cur_node] = pq.top();
		pq.pop();

		if (dists[cur_node] < cur_dist) continue;

		for (const auto& x : graph[cur_node]) {
			auto [next_dist, next_node] = x;
			long long new_dist = cur_dist + next_dist;

			if (dists[next_node] <= new_dist) continue;

			dists[next_node] = new_dist;
			pq.push({ new_dist, next_node });
		}
	}
}