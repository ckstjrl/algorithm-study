/*** 1854. K번째 최단경로 찾기 ***/

#include<iostream>
#include<vector>
#include<queue>
using namespace std;

void k_dijkstra(int start);

vector<pair<long long, int>> graph[1001];
priority_queue<long long> k_dist[1001];
int n, m, k;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> n >> m >> k;

	for (int i = 0; i < m; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		graph[a].push_back({ c, b });
	}

	k_dijkstra(1);

	for (int i = 1; i < n + 1; i++) {
		if (k_dist[i].size() < k) cout << -1 << '\n';
		else cout << k_dist[i].top() << '\n';
	}

	return 0;
}

void k_dijkstra(int start) {
	priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;

	pq.push({ 0, start });
	k_dist[start].push(0);

	while (!pq.empty()) {
		auto[dist, node] = pq.top();
		pq.pop();

		if (k_dist[node].size() == k && k_dist[node].top() < dist) continue;

		for (const auto& x : graph[node]) {
			auto[next_dist, next_node] = x;
			long long new_dist = dist + next_dist;
			
			/*
			k_dist[next_node].push(new_dist);
			if (k_dist[next_node].size() > k) k_dist[next_node].pop();
			pq.push({ new_dist, next_node });
			*/
			if (k_dist[next_node].size() < k || k_dist[next_node].top() > new_dist) {
				k_dist[next_node].push(new_dist);
				pq.push({ new_dist, next_node });
				if (k_dist[next_node].size() > k) k_dist[next_node].pop();
				
			}

		}
	}
}